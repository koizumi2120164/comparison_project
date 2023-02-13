#from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models

class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    class Meta:
        verbose_name_plural = 'CustomUser'

    YEAR = [
        ("1990","1990"),
        ("1991","1991"),
        ("1992","1992"),
        ("1993","1993"),
        ("1994","1994"),
        ("1995","1995"),
        ("1996","1996"),
        ("1997","1997"),
        ("1998","1998"),
        ("1999","1999"),
        ("2000","2000"),
        ("2001","2001"),
        ("2002","2002"),
        ("2003","2003"),
        ("2004","2004"),
        ("2005","2005"),
        ("2006","2006"),
        ("2007","2007"),
        ("2008","2008"),
        ("2009","2009"),
        ("2010","2010"),
    ]

    MONTH = [
        ("1月","1月"),
        ("2月","2月"),
        ("3月","3月"),
        ("4月","4月"),       
        ("5月","5月"),
        ("6月","6月"),
        ("7月","7月"),
        ("8月","8月"),
        ("9月","9月"),
        ("10月","10月"),
        ("11月","11月"),
        ("12月","12月"),
    ]

    DAY = [
        ("1日","1日"),
        ("2日","2日"),
        ("3日","3日"),
        ("4日","4日"),
        ("5日","5日"),
        ("6日","6日"),
        ("7日","7日"),
        ("8日","8日"),
        ("9日","9日"),
        ("10日","10日"),
        ("11日","11日"),
        ("12日","12日"),
        ("13日","13日"),
        ("14日","14日"),
        ("15日","15日"),
        ("16日","16日"),
        ("17日","17日"),
        ("18日","18日"),
        ("19日","19日"),
        ("20日","20日"),
        ("21日","21日"),
        ("22日","22日"),
        ("23日","23日"),
        ("24日","24日"),
        ("25日","25日"),
        ("26日","26日"),
        ("27日","27日"),
        ("28日","28日"),
        ("29日","29日"),
        ("30日","30日"),
        ("31日","31日"),
    ]


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
    user_birthday = models.DateField(verbose_name='年',choices=YEAR, blank=True, null=True)
    user_birthday_month = models.DateField(verbose_name='月',choices=MONTH, blank=True, null=True)
    user_birthday_day = models.DateField(verbose_name='日',choices=DAY, blank=True, null=True)
    user_gender = models.CharField(verbose_name="性別", choices=GENDER, blank=True, null=True, max_length=5)
    user_address = models.CharField(verbose_name='住所', choices=ADDRESS, max_length=50, blank=True, null=True)
    user_photo = models.ImageField(verbose_name='写真', blank=True, null=True)
    no_of_review = models.IntegerField(verbose_name='レビュー投稿数', default=0)
    no_of_word = models.IntegerField(verbose_name='口コミ投稿数', default=0)
    


# Create your models here.