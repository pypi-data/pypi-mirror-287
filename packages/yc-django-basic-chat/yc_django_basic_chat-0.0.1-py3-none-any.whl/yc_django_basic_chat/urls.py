"""
Created on 2024/7/19 下午4:59
@author:刘飞
@description:
"""
from django.urls import re_path
from rest_framework import routers
from .api.message_curd import MessageViewSet
from .api.conversation_curd import ConversationViewSet
from .api.az_models_curd import AzureOpenAIModelsViewSet
from .api.qa import Qa
from .api.qa_stream import QaStream

system_url = routers.SimpleRouter()
system_url.register(r'message', MessageViewSet, basename='message')
system_url.register(r'conversation', ConversationViewSet, basename='conversation')
system_url.register(r'azure_openai_models', AzureOpenAIModelsViewSet, basename='azure_openai_models')

urlpatterns = [
    re_path(r'^qa/', Qa.as_view(), name='qa'),
    re_path(r'^qa_stream/', QaStream.as_view(), name='qa_stream')
]
urlpatterns += system_url.urls
