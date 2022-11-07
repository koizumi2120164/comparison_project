from accounts.models import CustomUser
from django.db import models


class Diary(models.Model):
    """口コミ掲示板"""

    wordID = models.CharField(primarykey=True,verbose_name='口コミID', blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, verbose_name='投稿者', max_length=50, on_delete=models.PROTECT)
    review_title = models.CharField(verbose_name='口コミタイトル', max_length=100)
    review_text = models.TextField(verbose_name='口コミ内容', blank=True, null=True, max_length=250)
    review_text = models.DateTimeField(verbose_name='投稿日時', blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='更新日', blank=True, null=True)
    like_review = models.ManyToManyField(verbose_name='いいね', blank=True, null=True)   
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'project'

    def __str__(self):
        return self.title