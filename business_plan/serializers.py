from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework import serializers

from .models import *


class QuestionListSerializer(serializers.ModelSerializer):
    """Question list serializer."""
    class Meta:
        model = Question
        fields = ['text', 'section', 'offered_answer', 'type', 'is_active']
        depth = 2


class QuestionSerializer(serializers.ModelSerializer):
    """Question serializer."""
    class Meta:
        model = Question
        fields = ['id', 'text']


class OfferedAnswerSerializer(serializers.ModelSerializer):
    """Offered Answer serializer."""
    class Meta:
        model = OfferedAnswer
        fields = ['id', 'text']


class AnswerSerializer(serializers.ModelSerializer):
    """Answer serializer."""
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.select_related('type'))
    offered_answer = serializers.PrimaryKeyRelatedField(queryset=OfferedAnswer.objects.all(), required=False)

    class Meta:
        model = Answer
        fields = ['id', 'question', 'offered_answer', 'answer_positive_int']
        depth = 1

    @transaction.atomic
    def create(self, validated_data):
        """Create new answer instance"""
        business_plan = self.context['business_plan']
        Answer.objects.create(business_plan=business_plan, **validated_data)
        return validated_data

    @transaction.atomic
    def update(self, instance, validated_data):
        """Update answer instance."""
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance 


# class AnswerSerializer(serializers.ModelSerializer):
#     """"""
#     question = QuestionSerializer()
#     offered_answer = OfferedAnswerSerializer()

#     class Meta:
#         model = Answer
#         fields = ['id', 'question', 'offered_answer', 'answer_positive_int']
#         depth = 2


class BusinessPlanSerializer(serializers.ModelSerializer):
    """Business Plan serializer with related answers as nested serializer."""
    answers = AnswerSerializer(many=True)
    
    class Meta:
        model = BusinessPlan
        fields = ['id', 'answers']
        depth = 2

    def validate(self, data):
        """validate that answers for all given questions is submitted with the right answer type."""
        answers = data.get('answers')
        is_update = self.context['is_update']
        # validate that answers for all given questions is submitted in case of creation.
        if not is_update and len(answers) < Question.objects.count():
            raise serializers.ValidationError({"answers": 
                "You must answer all given questions"})
        # validate that each question type has the corresponding answer.
        for answer in answers:
            # Multiple Choice questions
            if answer['question'].type.name == 'Multiple Choice' and (
                not answer.get('offered_answer', None) or answer.get('answer_positive_int', None)):
                raise serializers.ValidationError({"answers": 
                    {"question": "You must answer with one of the offered answers only."}})
            # Positive number questions
            if answer['question'].type.name != 'Multiple Choice' and (
                answer.get('offered_answer', None) or not answer.get('answer_positive_int', None)):
                raise serializers.ValidationError({"answers": 
                    {"question": "You must answer with positive number only."}})           
        return data

    @transaction.atomic
    def create(self, validated_data):
        """Create new instance and related answers using nested serializer."""
        request = self.context['request']
        business_plan = BusinessPlan.objects.create(user=request.user)
        for answer in validated_data['answers']:
            AnswerSerializer.create(AnswerSerializer(context={
                "business_plan": business_plan, "request": request}), 
                                validated_data=answer)
        return business_plan

    @transaction.atomic
    def update(self, instance, validated_data):
        """Update instance and related answers using nested serializer."""
        if 'answers' in validated_data.keys():
            for answer in validated_data['answers']:
                answer_obj = get_object_or_404(Answer,
                    business_plan=instance, question=answer['question'])
                AnswerSerializer.update(AnswerSerializer(), instance=answer_obj, validated_data=answer)
        return instance