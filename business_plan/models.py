from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class BaseTimestamp(models.Model):
    """Timestamp abstract model."""
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Mata:
        abstract = True


class Section(BaseTimestamp):
    """Section model, inherits from basetimestamp abstract model."""
    name = models.CharField(_("Name"), max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Section")
        verbose_name_plural = _("Sections")

    def __str__(self):
        return f"{self.name}"


class Question(models.Model):
    """Question model."""
    text = models.CharField(_("Text"), max_length=255, unique=True)
    type = models.ForeignKey('QuestionType', on_delete=models.PROTECT, related_name="questions",
        verbose_name=_("Type"))
    section = models.ForeignKey(Section, on_delete=models.PROTECT, related_name="questions",
        verbose_name=_("Section"))   
    offered_answer = models.ManyToManyField("OfferedAnswer", verbose_name=_("Offered Answer"), blank=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return f"{self.section.name} | {self.text}"


class QuestionType(BaseTimestamp):
    """Question Type model, inherits from basetimestamp abstract model."""
    name = models.CharField(_("Name"), max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Question Type")
        verbose_name_plural = _("Question Types")

    def __str__(self):
        return f"{self.name}"


class OfferedAnswer(BaseTimestamp):
    """Offered Answer model, inherits from basetimestamp abstract model."""
    text = models.CharField(_("Text"), max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Offered Answer")
        verbose_name_plural = _("Offered Answers")

    def __str__(self):
        return f"{self.text}"


class Answer(models.Model):
    """Selected Answer model."""
    business_plan = models.ForeignKey('BusinessPlan', on_delete=models.PROTECT, related_name="answers",
        verbose_name=_("Business Plan"))
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name="answers",
        verbose_name=_("Question"))
    offered_answer = models.ForeignKey(OfferedAnswer, on_delete=models.PROTECT, related_name="answers",
        verbose_name=_("Offered Answer"), null=True, blank=True)
    answer_positive_int = models.PositiveIntegerField(verbose_name=_("Answer Positive Integer"),
        null=True, blank=True) 
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)    

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        unique_together = ['business_plan', 'question']

    def __str__(self):
        if self.offered_answer:
            return f"{self.business_plan} | {self.question.text} | {self.offered_answer.text}"
        return f"{self.business_plan} | {self.question.text} | {self.answer_positive_int}"    

    def clean(self):
        """Can't have null values or values for both offered_answer and answer_positive_int."""
        super().clean()
        # validate if offered_answer, answer_positive_int both have null values
        if not self.offered_answer and not self.answer_positive_int:
            raise ValidationError(_("Can't have null values for both offered answer and answer positive integer"))
        # validate if offered_answer, answer_positive_int both have values
        if self.offered_answer and self.answer_positive_int:
            raise ValidationError( _("Can't have values for both offered answer and answer positive integer"))


class BusinessPlan(BaseTimestamp):
    """Business Plan model, inherits from basetimestamp abstract model."""
    name = models.CharField(_("Name"), max_length=100)
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name="business_plans",
        verbose_name=_("User"))
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Business Plan")
        verbose_name_plural = _("Business Plans")
        unique_together = ['name', 'user']

    def __str__(self):
        return f"{self.name}| {self.user.username}"   
    