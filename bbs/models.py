from django.db import models
from django.utils import timezone
from accounts.models import CustomUser


class Post(models.Model):
    """投稿"""
    writer = models.CharField('投稿者', default='名無し', max_length=32)
    title = models.CharField('タイトル', max_length=256)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.title


class LikeForPost(models.Model):
    """投稿に対するいいね"""
    target = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

