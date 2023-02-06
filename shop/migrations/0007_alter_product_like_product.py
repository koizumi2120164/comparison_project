# Generated by Django 3.2.7 on 2023-02-02 02:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0006_auto_20230202_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='like_product',
            field=models.ManyToManyField(blank=True, null=True, related_name='product_like', to=settings.AUTH_USER_MODEL),
        ),
    ]