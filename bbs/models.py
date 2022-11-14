from django.db import models
from django.utils import timezone
from accounts.models import CustomUser


class Post(models.Model):
    writer = models.CharField('投稿者', default='名無し', max_length=32)
    title = models.CharField('タイトル', max_length=256)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.title


class LikeForPost(models.Model):
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    wished_item = models.ForeignKey(Post, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    added_date = models.DateTimeField(default=timezone.now)