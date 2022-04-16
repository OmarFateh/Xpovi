from django.urls import path

from .views import *


"""
CLIENT
BASE ENDPOINT /api/users/
"""

urlpatterns = [
    # Authentication
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    # path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    # Token
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]