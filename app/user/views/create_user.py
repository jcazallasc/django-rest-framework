from rest_framework import generics

from user.serializers.user import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user"""
    serializer_class = UserSerializer
