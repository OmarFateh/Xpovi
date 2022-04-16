from django.apps import AppConfig


class BusinessPlanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'business_plan'

    def ready(self):
        import business_plan.signals


    