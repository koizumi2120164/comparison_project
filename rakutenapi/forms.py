from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(label ='タタイトル', max_length=200, required = True)