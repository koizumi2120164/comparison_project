from django.db import models
from shop.models import *
import uuid
from accounts.models import *



class Word(models.Model):
    """口コミ掲示板"""

    wordID = models.UUIDField(default=uuid.uuid4, verbose_name='ワードID', editable=False)
    created_by = models.ForeignKey('accounts.CustomUser', verbose_name='投稿者', max_length=50, on_delete=models.PROTECT, related_name="created_by")
    word_title = models.CharField(verbose_name='口コミタイトル', max_length=100)
    word_text = models.TextField(verbose_name='口コミ内容', blank=True, null=True, max_length=250)
    created_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日',auto_now=True )
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)
    like_word = models.ManyToManyField('accounts.CustomUser', verbose_name='いいね', default=0, related_name="like_word")

    class Meta:
        verbose_name_plural = 'Word'

    def __str__(self):
        return self.word_title


class Review(models.Model):
    CHOICE = [ 
        ("1","★☆☆☆☆"),
        ("2","★★☆☆☆"),
        ("3","★★★☆☆"),
        ("4","★★★★☆"),
        ("5","★★★★★"), 
    ]

    reviewID = models.UUIDField(default=uuid.uuid4, verbose_name='レビューID', editable=False)
    created_by = models.ForeignKey('accounts.CustomUser', verbose_name='投稿者', on_delete=models.PROTECT, max_length=50, default=1, related_name="review_created_by")
    review = models.TextField(verbose_name="レビュー評価", choices=CHOICE, default=1, max_length=5)
    review_title = models.CharField(verbose_name='レビュータイトル', max_length=100)
    productID = models.ForeignKey(Product,verbose_name='商品ID', on_delete=models.PROTECT, blank=True, null=True, max_length=50)
    review_text = models.TextField(verbose_name='レビュー内容', blank=True, null=True, max_length=250)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日', auto_now=True)
    like_review = models.ManyToManyField('accounts.CustomUser', verbose_name='いいね', default=0, related_name="like_review")

    class Meta:
        verbose_name_plural = 'Review'

    def __str__(self):
        return self.review_title


class Recently_viewed(models.Model):
    userID = models.ForeignKey('accounts.CustomUser', verbose_name='ユーザーID', on_delete=models.PROTECT, max_length=50, default=1)
    productID = models.ForeignKey('shop.Product',verbose_name='商品ID', on_delete=models.PROTECT, max_length=50)
    last_visited = models.DateTimeField(verbose_name='更新日', auto_now=True)


class Wishlist(models.Model):
    userID = models.ForeignKey('accounts.CustomUser', verbose_name='ユーザーID', on_delete=models.PROTECT, default=1)
    wished_item = models.ForeignKey('shop.Product', verbose_name='商品ID', on_delete=models.PROTECT, default=1)
    slug = models.SlugField(verbose_name='管理番号', max_length=255, unique=True)
    added_date = models.DateTimeField(verbose_name='追加された日時', auto_now=True)