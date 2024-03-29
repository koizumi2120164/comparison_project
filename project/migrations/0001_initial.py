# Generated by Django 3.2.7 on 2023-01-25 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0004_auto_20221117_1553'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0004_auto_20221117_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='ユーザーID')),
                ('wished_item', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='商品ID')),
                ('slug', models.SlugField(verbose_name='管理番号')),
                ('added_date', models.DateTimeField(auto_now=True, verbose_name='追加された日時')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewID', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='レビューID')),
                ('review', models.TextField(choices=[('1', '★☆☆☆☆'), ('2', '★★☆☆☆'), ('3', '★★★☆☆'), ('4', '★★★★☆'), ('5', '★★★★★')], default=1, max_length=5, verbose_name='レビュー評価')),
                ('review_title', models.CharField(max_length=100, verbose_name='レビュータイトル')),
                ('review_text', models.TextField(blank=True, max_length=250, null=True, verbose_name='レビュー内容')),
                ('review_photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真')),
                ('review_created_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('review_updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('review_created_by', models.ForeignKey(default=1, max_length=50, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
                ('review_productID', models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='商品ID')),
            ],
        ),
        migrations.CreateModel(
            name='Recently_viewed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_visited', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('productID', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='商品ID')),
                ('userID', models.ForeignKey(default=1, max_length=50, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザーID')),
            ],
        ),
    ]
