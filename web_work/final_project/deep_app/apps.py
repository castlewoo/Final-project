from django.apps import AppConfig


<<<<<<<< HEAD:web_work/final_project/deep_app/apps.py
class DeepAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'deep_app'
========
class {{ camel_case_app_name }}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{ app_name }}'
>>>>>>>> 8e17d8ae57b448f400d2cee7c0086496ea51f23e:web_work/venv/Lib/site-packages/django/conf/app_template/apps.py-tpl
