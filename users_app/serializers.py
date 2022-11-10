from rest_framework.serializers import ModelSerializer
from .models import UsersModel


class UsersSerializers(ModelSerializer):
    class Meta:
        model = UsersModel
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar']