# Generated by Django 3.2.7 on 2022-09-20 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='カテゴリー')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='タイトル')),
                ('address', models.CharField(max_length=255, verbose_name='住所')),
                ('description', models.TextField(blank=True, null=True, verbose_name='物件情報')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真3')),
                ('slug', models.SlugField(max_length=255)),
                ('is_vacant', models.BooleanField(default=True, verbose_name='空室あり')),
                ('conditions', models.CharField(max_length=255, verbose_name='入居条件')),
                ('rent_price', models.CharField(max_length=40, verbose_name='家賃個室')),
                ('utility_fee', models.CharField(max_length=40, verbose_name='共益費')),
                ('admin_fee', models.CharField(max_length=40, verbose_name='事務手数料')),
                ('station', models.TextField(blank=True, null=True, verbose_name='最寄り駅')),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='map.category', verbose_name='カテゴリー')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_creator', to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
    ]
