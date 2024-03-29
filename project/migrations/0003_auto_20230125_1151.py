# Generated by Django 3.2.7 on 2023-01-25 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_word'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_created_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='review_created_by',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='review_photo',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='review_productID',
            new_name='productID',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='review_updated_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='word',
            old_name='word_created_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='word',
            old_name='word_created_by',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='word',
            old_name='word_photo',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='word',
            old_name='word_updated_at',
            new_name='updated_at',
        ),
    ]
