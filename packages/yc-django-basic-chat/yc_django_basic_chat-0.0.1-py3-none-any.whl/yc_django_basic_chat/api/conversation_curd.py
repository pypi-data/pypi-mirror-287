"""
Created on 2024/7/22 下午3:18
@author:刘飞
@description:
"""
from yc_django_utils.viewset import CustomModelViewSet
from ..models import Conversation
from ..serializers import ConversationSerializer


class ConversationViewSet(CustomModelViewSet):
    http_method_names = ['get']
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_fields = ['id', 'name']
