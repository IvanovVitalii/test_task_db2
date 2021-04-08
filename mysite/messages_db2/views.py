from django.shortcuts import render
from rest_framework import generics
from .serializers import MessageDetailSerializer


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageDetailSerializer