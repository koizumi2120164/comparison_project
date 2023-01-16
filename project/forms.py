from django import forms
from .models import *
from shop.models import *
from accounts.models import CustomUser
from .models import Word
# from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('review','review_title', 'review_text', 'photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ItemForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'image1', 'image2', 'image3',
                  'price1', 'link1', 'price2', 'link2', 'price3', 'link3',
                  'rating', 'like_product', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('user_photo','user_name', 'user_birthday', 'user_gender', 'user_address')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'



class WordCreateForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ('Word_title','Word_text','photo',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'