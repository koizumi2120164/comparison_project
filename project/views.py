from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "index.html"


class SearchView(generic.TemplateView):
    template_name = "search.html"


class SearchResultsView(generic.TemplateView):
    template_name = "search_results.html"

    def get_nyuuryoku(request):

        keyword = request.GET.get("keyword")
        brand = request.GET.get("brand")
        value = request.GET.get("value")
        display = request.GET.get("display")

        return keyword,brand,value,display
        