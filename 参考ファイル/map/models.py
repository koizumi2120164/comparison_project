from accounts.models import CustomUser
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    """カテゴリーモデル"""
    name = models.CharField(verbose_name='カテゴリー', max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse('map:category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', verbose_name='カテゴリー', on_delete=models.PROTECT)
    created_by = models.ForeignKey(CustomUser, related_name='product_creator', verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    address = models.CharField(verbose_name='住所', max_length=255)
    description = models.TextField(verbose_name='物件情報', blank=True, null=True)
    image1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    image2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    image3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_vacant = models.BooleanField(default=True, verbose_name='空室あり')
    conditions = models.CharField(verbose_name='入居条件', max_length=255)
    rent_price = models.CharField(verbose_name='家賃個室', max_length=40)
    utility_fee = models.CharField(verbose_name='共益費', max_length=40)
    admin_fee = models.CharField(verbose_name='事務手数料', max_length=40)
    station = models.TextField(verbose_name='最寄り駅', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True, blank=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse('map:detail', args=[self.slug])

    def __str__(self):
        return self.title