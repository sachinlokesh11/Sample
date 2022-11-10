from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UsersModel
from .serializers import UsersSerializers
# Create your views here.


class UsersList(ListAPIView):
    queryset = UsersModel.objects.all()
    serializer_class = UsersSerializers


class Users(APIView):

    def get(self, request, pk):
        user = get_object_or_404(UsersModel.objects.all(), pk=pk)
        serializer = UsersSerializers(user)
        return Response(serializer.data)




