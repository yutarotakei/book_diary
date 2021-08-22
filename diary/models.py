from django.db import models
from accounts.models import CustomUser


class Book(models.Model):

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    author = models.CharField(verbose_name='著者', max_length=40)
    type = models.CharField(verbose_name='種別', max_length=40)
    genre = models.CharField(verbose_name='ジャンル', max_length=40)
    read_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Book'

    def __str__(self):
        return self.title
