from django.shortcuts import render

# Create your views here.

# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets


from earthmiles.serializers import SnippetSerializer
from earthmiles.models import Snippet
from rest_framework import generics

# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#


