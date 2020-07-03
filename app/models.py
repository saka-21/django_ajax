from django.db import models
from time import timezone


class Post(models.Model):
   title = models.CharField('タイトル', max_length=50)
   text = models.TextField('本文')
   image = models.ImageField('画像', upload_to='images', blank=True)
   created_at = models.DateTimeField('投稿日', default=timezone.now)
   tag = models.ForeignKey(Tag, verbose_name='タグ', on_delete=models.PROTECT)
   user = models.ForeignKey(User, on_delete=models.CASCADE) #追加
   like = models.ManyToManyField(User, related_name='like', blank=True)
   def __str__(self):
       return self.title #省略