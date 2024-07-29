"""
Created on 2024/7/23 上午10:05
@author:刘飞
@description: 问答
"""
from rest_framework.views import APIView
from yc_django_utils.validator import CustomValidationError
from yc_django_utils.json_response import DetailResponse
from ..helper import AzureOpenAIClient


class Qa(APIView):
    def post(self, request, *args, **kwargs):
        model_id = request.data.get('model_id')
        conversation_id = request.data.get('conversation_id')
        question = request.data.get('question')
        if not all([model_id, conversation_id, question]):
            raise CustomValidationError('参数缺失')
        azure = AzureOpenAIClient(model_id, conversation_id)
        res_data = azure.chat(question=question, request=request)
        return DetailResponse(data=res_data)
