"""
Created on 2024/7/23 下午4:48
@author:刘飞
@description:
"""
from django.http import StreamingHttpResponse
from rest_framework.views import APIView
from yc_django_utils.validator import CustomValidationError
from ..helper import AzureOpenAIClient


class QaStream(APIView):
    def post(self, request, *args, **kwargs):
        model_id = request.data.get('model_id')
        conversation_id = request.data.get('conversation_id')
        question = request.data.get('question')
        if not all([model_id, conversation_id, question]):
            raise CustomValidationError('参数缺失')
        azure = AzureOpenAIClient(model_id, conversation_id)
        # 流式出传输
        response = StreamingHttpResponse(
            azure.chat_stream(question=question, request=request),
            content_type="text/event-stream")
        # 设置响应头，告诉浏览器我们将会多次发送数据
        response['Cache-Control'] = 'no-cache'
        # response['Content-Type'] = 'text/event-stream;charset=utf-8'
        return response
