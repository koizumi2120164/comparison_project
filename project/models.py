from django.db import models


class Review(models.Model):
    """レビューモデル"""

    reviewID = models.UUIDField(verbose_name='レビューID', primary_key=True, editable=False)
    created_by = models.ForeignKey(userID, verbose_name='投稿者', on_delete=models.PROTECT, max_length=50)
    review = models.IntegerField(verbose_name='レビュー', required=True)
    review_title = models.CharField(verbose_name='レビュータイトル', max_length=100)
    productID = models.ForeignKey(verbose_name='商品ID', on_delete=models.PROTECT, max_length=50)
    review_text = models.TextField(verbose_name='レビュー内容', blank=True, null=True, max_length=250)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日', auto_now=True)
    like_review = models.ManyToManyField(verbose_name='いいね', )
