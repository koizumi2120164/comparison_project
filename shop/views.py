from django.shortcuts import render
from django.views.generic import View
from .forms import SearchForm
import json
import requests

SEARCH_URL = 'https://app.rakuten.co.jp/services/api/BooksTotal/Search/20170404?format=json&applicationId=[1059665974949401126]'

def get_api_data(params):
    api = requests.get(SEARCH_URL, params=params).text
    result = json.loads(api)
    items = result['Items']
    return items

class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = SearchForm(request.POST or None)

        return render(request, 'testindex.html', {
            'form':form,
        })
    
