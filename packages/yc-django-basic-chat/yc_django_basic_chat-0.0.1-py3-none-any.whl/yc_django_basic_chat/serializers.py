"""
Created on 2024/7/19 下午4:59
@author:刘飞
@description:
"""

from yc_django_utils.serializers import CustomModelSerializer
from .models import AzureOpenAIModels, Conversation, Message


class AzureOpenAIModelsSerializer(CustomModelSerializer):
    class Meta:
        model = AzureOpenAIModels
        read_only_fields = ['id']
        exclude = ['api_key']


class AzureOpenAIModelsCreateSerializer(CustomModelSerializer):
    class Meta:
        model = AzureOpenAIModels
        fields = '__all__'
        read_only_fields = ['id']


class ConversationSerializer(CustomModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'
        read_only_fields = ['id']


class MessageSerializer(CustomModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['id']
