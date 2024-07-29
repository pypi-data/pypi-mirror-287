from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from yc_django_utils.models import BaseModel

User = get_user_model()

table_prefix = settings.TABLE_PREFIX


class Conversation(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("名称"))

    class Meta:
        verbose_name = _("会话")
        verbose_name_plural = _("会话")
        db_table = f"{table_prefix}_basic_chat_conversation"
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Message(BaseModel):
    """
    会话消息
    """
    start_context = [
        {"role": "system", "content": "You are a helpful assistant"}
    ]
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, verbose_name=_("关联会话"))
    question_text = models.TextField(verbose_name=_("问题文本"), default="")
    answer_text = models.TextField(verbose_name=_("回答文本"), blank=True, null=True)
    context = models.JSONField(verbose_name=_("上下文"), blank=True, null=True, default=start_context)
    response_metadata = models.JSONField(verbose_name=_("响应标签"), blank=True, null=True)
    usage_metadata = models.JSONField(verbose_name=_("token使用信息"), blank=True, null=True)
    response_id = models.CharField(max_length=255, verbose_name=_("会话id"), blank=True, null=True)
    resource_data = models.JSONField(verbose_name=_("原生返回数据"), blank=True, null=True)

    class Meta:
        verbose_name = _("消息")
        verbose_name_plural = _("消息")
        db_table = f"{table_prefix}_basic_chat_message"
        ordering = ('-id',)

    def __str__(self):
        return self.question_text


class AzureOpenAIModels(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("部署名称"))
    api_key = models.CharField(max_length=255, verbose_name=_("API Key"))
    api_base = models.CharField(max_length=255, verbose_name=_("API Base"))
    api_version = models.CharField(max_length=255, verbose_name=_("API Version"))
    api_type = models.CharField(max_length=255, verbose_name=_("API Type"), default="Chat")
    temperature = models.FloatField(verbose_name=_('阈值'), default=0.7)
    max_tokens = models.IntegerField(verbose_name=_('允许最大token值'), default=4096)
    is_active = models.BooleanField(default=True, verbose_name=_("是否激活"))

    class Meta:
        verbose_name = _("Azure OpenAI 模型")
        verbose_name_plural = _("Azure OpenAI 模型")
        db_table = f"{table_prefix}_basic_chat_azure_openai_models"
        ordering = ('-id',)

    def __str__(self):
        return self.name
