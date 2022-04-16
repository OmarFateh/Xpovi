from rest_framework import generics, status #,mixins, permissions
# from rest_framework.views import APIView
from rest_framework.response import Response

from .permissions import AnonPermissionOnly
from .models import User
from .serializers import UserRegisterationSerializer, UserLoginSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    """User registeration API view."""
    permission_classes = [AnonPermissionOnly]
    queryset = User.objects.all()
    serializer_class = UserRegisterationSerializer
    
    # def get_serializer_context(self, *args, **kwargs):
    #     return {"request": self.request}


class UserLoginAPIView(generics.GenericAPIView):
    """User login API view."""
    permission_classes = [AnonPermissionOnly]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)