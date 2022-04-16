from django.contrib import admin

from .models import *


admin.site.register(Section)
admin.site.register(Question)
admin.site.register(QuestionType)
admin.site.register(OfferedAnswer)
admin.site.register(Answer)
admin.site.register(BusinessPlan)