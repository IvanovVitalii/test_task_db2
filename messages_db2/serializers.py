from rest_framework import serializers
from .models import Message


class MessagesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
