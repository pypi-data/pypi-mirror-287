"""
Created on 2024/7/22 下午3:19
@author:刘飞
@description:
"""
from yc_django_utils.viewset import CustomModelViewSet
from ..models import Message
from ..serializers import MessageSerializer


class MessageViewSet(CustomModelViewSet):
    http_method_names = ['get']
    # queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_fields = ['conversation']
    search_fields = ['conversation']

    def get_queryset(self):
        """
        重写get_queryset方法，根据conversation_pk获取会话下的消息
        :return:
        """
        conversation_id = self.request.query_params.get('conversation_id')
        if not conversation_id:
            return Message.objects.none()
        return Message.objects.filter(conversation_id=conversation_id)
