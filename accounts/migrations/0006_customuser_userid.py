# Generated by Django 3.2.7 on 2022-12-02 00:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20221128_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='userID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='ユーザーID'),
        ),
    ]
