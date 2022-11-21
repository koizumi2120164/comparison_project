# Generated by Django 3.2.7 on 2022-11-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_review_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(choices=[('★', '1'), ('★', '2'), ('★', '3'), ('★', '4'), ('★', '5')], default=1, max_length=5, verbose_name='レビュー評価'),
        ),
    ]