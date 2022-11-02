from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"

class SearchView(generic.TemplateView):
    template_name = "search.html"
    