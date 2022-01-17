from django.urls import path
from .views import CreateUserAPIView, authenticate_user, UserRetrieveUpdateAPIView

urlpatterns = [
    path(r'^create/$', CreateUserAPIView.as_view()),
    path(r'^update/$', UserRetrieveUpdateAPIView.as_view()),
    path(r'^obtain_token/$', authenticate_user),

]