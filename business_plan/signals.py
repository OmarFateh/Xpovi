from django.dispatch import receiver
from django.db.models.signals import pre_save

from .utils import generate_unique_name
from .models import BusinessPlan 


@receiver(pre_save, sender=BusinessPlan)
def set_business_plan_name(sender, instance, *args, **kwargs):
    """Set business plan unique name."""
    if instance:
        instance.name = generate_unique_name(instance)