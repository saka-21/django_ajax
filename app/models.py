# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tag(models.Model):
    tag = models.CharField(verbose_name='タグ名', max_length=50)

    def __str__(self):
        return self.tag


class Post(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=35)
    text = models.TextField(verbose_name='本文')
    image = models.ImageField(verbose_name='画像', upload_to='images', blank=True)
    created_at = models.DateTimeField(verbose_name='投稿日', default=timezone.now)
    tag = models.ForeignKey(Tag, verbose_name='タグ', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 追加

    def __str__(self):
        return self.title
