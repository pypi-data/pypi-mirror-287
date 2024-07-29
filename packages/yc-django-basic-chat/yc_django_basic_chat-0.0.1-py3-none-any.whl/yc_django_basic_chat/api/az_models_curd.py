"""
Created on 2024/7/22 下午3:18
@author:刘飞
@description:
"""
from yc_django_utils.viewset import CustomModelViewSet
from ..models import AzureOpenAIModels
from ..serializers import AzureOpenAIModelsSerializer, AzureOpenAIModelsCreateSerializer


class AzureOpenAIModelsViewSet(CustomModelViewSet):

    queryset = AzureOpenAIModels.objects.all()
    create_serializer_class = AzureOpenAIModelsCreateSerializer
    serializer_class = AzureOpenAIModelsSerializer
    filter_fields = ['name', 'is_active']
    search_fields = ['name', 'is_active']
