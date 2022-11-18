from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import CustomUser
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    """カテゴリーモデル"""
    category_name = models.CharField(verbose_name='カテゴリー', max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('project:category_list', args=[self.slug])

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(verbose_name='商品名', max_length=255)
    description = models.TextField(verbose_name='詳細', max_length=500)
    image1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    image2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    image3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    price1 = models.DecimalField(verbose_name='Amazon価格', max_digits=6, decimal_places=3, blank=True, null=True, default=0)
    link1 = models.CharField(verbose_name='Amazon店舗に飛ぶ', max_length=500, blank=True, null=True)
    price2 = models.DecimalField(verbose_name='楽天価格', max_digits=6, decimal_places=3, blank=True, null=True, default=0)
    link2 = models.CharField(verbose_name='楽天店舗に飛ぶ', max_length=500, blank=True, null=True)
    price3 = models.DecimalField(verbose_name='Yahooショッピング価格', max_digits=6, decimal_places=3, blank=True, null=True, default=0)
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
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)

    def number_of_likes(self):
        return self.like_product.count()

    def get_absolute_url(self):
        return reverse('project:product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name, allow_unicode=True)
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.product_name