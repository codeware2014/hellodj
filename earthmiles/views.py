from django.shortcuts import render

# Create your views here.

from earthmiles.models import Snippet
from earthmiles.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
import earthmiles.permissions


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, earthmiles.permissions.IsOwnerOrReadOnly)

    def pre_save(self, obj):
        obj.owner = self.request.user
        pass


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,  earthmiles.permissions.IsOwnerOrReadOnly)

    def pre_save(self, obj):
        obj.owner = self.request.user
        pass



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

