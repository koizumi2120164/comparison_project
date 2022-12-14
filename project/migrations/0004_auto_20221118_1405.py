# Generated by Django 3.2.7 on 2022-11-18 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20221117_1553'),
        ('project', '0003_review_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, max_length=5, verbose_name='レビュー評価'),
        ),
        migrations.AlterField(
            model_name='review',
            name='productID',
            field=models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='商品ID'),
        ),
    ]
