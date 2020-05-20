from django.contrib.auth import get_user_model
from rest_framework import generics

from core.views.base_auth import BaseAuthView
from user.serializers.user import UserSerializer


class DetailUserView(BaseAuthView, generics.ListAPIView):
    """List transactions by account"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(email=self.request.user)
