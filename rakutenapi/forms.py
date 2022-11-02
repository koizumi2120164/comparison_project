from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(label ='商品名', max_length=200, required = True)