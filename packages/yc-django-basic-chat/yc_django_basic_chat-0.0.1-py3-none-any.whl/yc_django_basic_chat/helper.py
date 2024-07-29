"""
Created on 2024/7/19 下午5:26
@author:刘飞
@description:
"""
import logging
from langchain_openai import AzureChatOpenAI
from yc_django_utils.validator import CustomValidationError
from .models import AzureOpenAIModels, Conversation, Message

logger = logging.getLogger()


class AzureOpenAIClient:
    def __init__(self, model_id, conversation_id):
        self.conversation_id = conversation_id
        self.azure_openai_model = AzureOpenAIModels.objects.filter(id=model_id).first()
        if not self.azure_openai_model:
            raise CustomValidationError("azure openai model not found")
        # 定义AzureOpenAI客户端
        self.llm = AzureChatOpenAI(
            azure_endpoint=self.azure_openai_model.api_base,
            openai_api_key=self.azure_openai_model.api_key,
            api_version=self.azure_openai_model.api_version,
            temperature=self.azure_openai_model.temperature,
            azure_deployment=self.azure_openai_model.name,
            max_tokens=self.azure_openai_model.max_tokens,
            max_retries=2,
        )

    def chat(self, question, request=None):
        """
        直接回答问题
        :param question:
        :param request:
        :return:
        """
        # 构造当前问题
        current_question = {"role": "human", "content": question}
        # 获取+构造当前会话的上下文
        message_obj = Message.objects.filter(conversation_id=self.conversation_id).first()
        if not message_obj:
            message_obj = Message.objects.create(conversation_id=self.conversation_id)
        context = message_obj.context
        context.append(current_question)

        # 调用会话接口
        response = self.llm.invoke(context)

        # 构造会话历史及相关其他信息
        current_answer = {"role": "assistant", "content": response.content}
        context.append(current_answer)

        # 构造和保存返回记录
        messages_conditions = {
            "conversation_id": self.conversation_id,
            "question_text": question,
            "answer_text": response.content,
            "context": context,
            "response_metadata": response.response_metadata,
            "usage_metadata": response.usage_metadata,
            "response_id": response.id,
            "resource_data": response.to_json(),
        }
        if request:
            messages_conditions["creator"] = request.user
            messages_conditions["modifier"] = request.user
        Message.objects.create(**messages_conditions)
        return response.content

    def chat_stream(self, question, request=None):
        """
        流式问答
        :param question:
        :param request:
        :return:
        """
        # 构造当前问题
        current_question = {"role": "human", "content": question}
        # 获取+构造当前会话的上下文
        message_obj = Message.objects.filter(conversation_id=self.conversation_id).first()
        if not message_obj:
            message_obj = Message.objects.create(conversation_id=self.conversation_id)
        context = message_obj.context
        context.append(current_question)

        # 调用会话接口
        answer = ""
        response_metadata = {}
        usage_metadata = {"input_tokens": 0, "total_tokens": 0, "output_tokens": 0}
        response_id = None
        for chunk in self.llm.stream(context):
            if chunk.response_metadata and chunk.response_metadata.get("finish_reason") == "stop":
                response_metadata = chunk.response_metadata
                response_id = chunk.id
            else:
                answer += chunk.content
                # yield f"data: {chunk.content}\n\n"
                yield f"data: {chunk}\n\n"

        # 构造会话历史及相关其他信息
        current_answer = {"role": "assistant", "content": answer}
        context.append(current_answer)
        for i in context:  # 计算token
            if i.get("role") == "human":
                usage_metadata["input_tokens"] += self.llm.get_num_tokens(i.get("content"))
            elif i.get("role") == "assistant":
                usage_metadata["output_tokens"] += self.llm.get_num_tokens(i.get("content"))
        usage_metadata["total_tokens"] = usage_metadata["input_tokens"] + usage_metadata["output_tokens"]

        # 构造和保存返回记录
        messages_conditions = {
            "conversation_id": self.conversation_id,
            "question_text": question,
            "answer_text": answer,
            "context": context,
            "response_metadata": response_metadata,
            "usage_metadata": usage_metadata,
            "response_id": response_id,
            "resource_data": {},
        }
        if request:
            messages_conditions["creator"] = request.user
            messages_conditions["modifier"] = request.user
        Message.objects.create(**messages_conditions)
