from django.contrib import admin
from .models import Message, Conversation, AzureOpenAIModels


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'conversation', 'question_text', 'answer_text', 'usage_metadata', 'response_id')
    list_display_links = ('id', 'conversation', 'question_text')
    list_filter = ['conversation']
    search_fields = ('conversation', 'question_text')
    ordering = ('-id',)
    readonly_fields = ('id',)


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    ordering = ('-id',)
    readonly_fields = ('id',)


@admin.register(AzureOpenAIModels)
class AzureOpenAIModelsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'api_base', 'api_key', 'api_type', 'api_version', 'is_active', 'max_tokens', 'temperature')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'is_active')
    search_fields = ('name', 'is_active')
    ordering = ('-id',)
    readonly_fields = ('id',)
