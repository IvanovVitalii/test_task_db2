from django.db import models
from django.core.validators import MinLengthValidator


class Message(models.Model):
    author = models.EmailField(verbose_name='Автор', db_index=True, max_length=254)
    massage = models.TextField(verbose_name='Сообщение', max_length=1024, validators=[MinLengthValidator(100)])
    created = models.DateTimeField(auto_now_add=True)
