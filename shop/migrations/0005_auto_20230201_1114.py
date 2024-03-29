# Generated by Django 3.2.7 on 2023-02-01 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20221117_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price1',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=10, null=True, verbose_name='Amazon価格'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price2',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=10, null=True, verbose_name='楽天価格'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price3',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=10, null=True, verbose_name='Yahooショッピング価格'),
        ),
    ]
