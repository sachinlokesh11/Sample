from django.urls import path
from .views import Users, UsersList

urlpatterns = [
    path('users/', UsersList.as_view()),
    path('users/<pk>', Users.as_view()),
]
