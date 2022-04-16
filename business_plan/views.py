from rest_framework import generics
from rest_framework.response import Response

from .serializers import * 


class QuestionListAPIView(generics.ListAPIView):
    """Question list API view."""
    queryset = Question.objects.select_related(
        'type', 'section').prefetch_related('offered_answer')
    serializer_class = QuestionListSerializer


class BusinessPlanCreateAPIView(generics.CreateAPIView):
    """BusinessPlan create API view."""
    queryset = BusinessPlan.objects.select_related('user')
    serializer_class = BusinessPlanSerializer

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request, "is_update": False}


class BusinessPlanRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """Business Plan retrieve update API view."""
    serializer_class = BusinessPlanSerializer

    def get_queryset(self, *args, **kwargs):
        """
        Return a list of all the business plans
        for the currently authenticated user.
        """
        return BusinessPlan.objects.select_related(
            'user').filter(user=self.request.user)

    def get_serializer_context(self, *args, **kwargs):
        return {"is_update": True}        