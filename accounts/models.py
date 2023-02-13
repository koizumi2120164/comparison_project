#from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models

class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    class Meta:
        verbose_name_plural = 'CustomUser'

    GENDER = [ 
        ("男性","男性"),
        ("女性","女性"),
    ]

    ADDRESS = [
        ("関東", "関東"),
        ("関西", "関西"),
        ("その他", "その他"),
    ]

    user_name = models.CharField(verbose_name='ユーザー名', max_length=120, default="")
    user_birthday = models.DateField(verbose_name='誕生日', blank=True, null=True)
    user_gender = models.CharField(verbose_name="性別", choices=GENDER, blank=True, null=True, max_length=5)
    user_address = models.CharField(verbose_name='住所', choices=ADDRESS, max_length=50, blank=True, null=True)
    user_photo = models.ImageField(verbose_name='写真', blank=True, null=True)
    no_of_review = models.IntegerField(verbose_name='レビュー投稿数', default=0)
    no_of_word = models.IntegerField(verbose_name='口コミ投稿数', default=0)
    


# Create your models here.