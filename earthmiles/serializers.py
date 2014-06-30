__author__ = 'Som'


from rest_framework import serializers
from earthmiles.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User



class SnippetSerializer(serializers.ModelSerializer):

    ownerName =serializers.Field(source = 'owner.username')

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'ownerName')# , 'url') #, 'highlight')




class UserSerializer(serializers.ModelSerializer):

    snippetList =  SnippetSerializer(source = 'snippets', many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets', 'snippetList')#, 'url')
        depth = 1
