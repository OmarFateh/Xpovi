from django.urls import path

from .views import *


"""
CLIENT
BASE ENDPOINT /api/business-plan/
"""

urlpatterns = [
    # Questions
    path('questions/', QuestionListAPIView.as_view(), name='questions'),
    # Business Plan
    path('create/', BusinessPlanCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', BusinessPlanRetrieveUpdateAPIView.as_view(), name='detail-update'),
    
]