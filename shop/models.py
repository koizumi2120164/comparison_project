from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import CustomUser

# Create your models here.
class Category(models.Model):
    """カテゴリーモデル"""
    category_name = models.CharField(verbose_name='カテゴリー', max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(verbose_name='商品名', max_length=250)
    description = models.TextField(verbose_name='詳細', max_length=500)
    image1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    image2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    image3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    price1 = models.CharField(verbose_name='Amazon価格', max_length=40, blank=True, null=True)
    link1 = models.CharField(verbose_name='Amazon店舗に飛ぶ', max_length=500, blank=True, null=True)
    price2 = models.CharField(verbose_name='楽天価格', max_length=40, blank=True, null=True)
    link2 = models.CharField(verbose_name='楽天店舗に飛ぶ', max_length=500, blank=True, null=True)
    price3 = models.CharField(verbose_name='Yahooショッピング価格', max_length=40, blank=True, null=True)
    link3 = models.CharField(verbose_name='Yahooショッピング店舗に飛ぶ', max_length=500, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='product', verbose_name='カテゴリー', on_delete=models.PROTECT)
    rating = models.IntegerField(verbose_name='商品評価', default='0',
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ])
    like_product = models.ManyToManyField(CustomUser, related_name='product_like')
    slug = models.SlugField(max_length=255, unique=True)
    product_brand = models.TextField(verbose_name='商品ブランド', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True, blank=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)

    def number_of_likes(self):
        return self.like_product.count()
    
    def __str__(self):
        return self.title