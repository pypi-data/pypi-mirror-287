"""
Created on 2024/7/19 下午5:01
@author:刘飞
@description:
"""
from django.utils.translation import gettext_lazy as _

basic_chat_menu_list = [
    {
        'name': _('Basic Chat'),
        'models': [
            {
                'name': _('模型管理'),
                'url': 'yc_django_basic_chat/azureopenaimodels/'
            },
            {
                'name': _('会话管理'),
                'url': 'yc_django_basic_chat/conversation/'
            },
            {
                'name': _('消息管理'),
                'url': 'yc_django_basic_chat/message/'
            }
        ]
    }
]
