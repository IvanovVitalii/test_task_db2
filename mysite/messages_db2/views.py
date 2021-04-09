from rest_framework import generics
from .serializers import MessageDetailSerializer, MessagesListSerializer
from .models import Message
from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 10


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageDetailSerializer


class MessagesListView(generics.ListAPIView):
    serializer_class = MessagesListSerializer
    queryset = Message.objects.all()
    pagination_class = ProductPagination


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageDetailSerializer
    queryset = Message.objects.all()
