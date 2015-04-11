from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import viewsets,status,generics
from rest_framework.views import APIView
from serializers import UserListSerializer,UserAuthSerializer,UserDetailSerializer
from django.contrib.auth import login, logout
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
import json
from rest_framework.decorators import api_view

#class UserView(viewsets.ModelViewSet):
#	queryset = User.objects.all()
#	serializer_class = UserSerializer
#	model = User

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


#redundant class
class UserSignup(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer	

class AuthView(APIView):

#	def get(self,request,format=None):
#  		users = User.objects.all()
#  		serializer = UserSerializer(users,many=True)
#  		return Response(serializer.data)

 	def post(self, request, format=None):
		user = authenticate(username=request.data['username'], password=request.data['password'])
		resDict = {"message": "Failed to authenticate"}
		if user is None:
			return Response(data=resDict, status=status.HTTP_200_OK)
		login(request, user)
		resDict["message"] = "Logged in successfully"
		return Response(data=resDict, status=status.HTTP_200_OK)

@api_view(['GET', ])
def logoutView(request):
	logout(request)
	resDict = {}
	resDict["message"] = "Logged out!"
	return Response(data=resDict, status=status.HTTP_200_OK)

