from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class BaseAuthView:
    """Base Auth View"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
