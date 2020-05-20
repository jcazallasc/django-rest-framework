from django.urls import path

from user.views.create_token import CreateTokenView
from user.views.create_user import CreateUserView
from user.views.detail_user import DetailUserView

app_name = 'user'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('detail/', DetailUserView.as_view(), name='detail'),
    path('token/', CreateTokenView.as_view(), name='token'),
]
