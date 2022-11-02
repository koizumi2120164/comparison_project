from django.shortcuts import render
from django.views.generic import View
from .forms import SearchForm
import requests

class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = SearchForm(request.POST or None)

        return render(request, 'app/index.html', {
            'form':form,
        })