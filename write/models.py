from django.db import models
from django.contrib.auth.models import User

class Wave(models.Model):
    user = models.ForeignKey(User, on_delete=None)
    description = models.CharField(max_length=300, verbose_name='Описание')
    money = models.IntegerField(verbose_name='Сумма')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.description
