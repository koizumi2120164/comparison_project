from django.views import generic
from django.contrib import messages
from .models import Review
from .forms import ReviewForm


class IndexView(generic.TemplateView):
    template_name = "index.html"


class SearchAdvancedView(generic.TemplateView):
    template_name = "search.html"


class SearchResultsView(generic.TemplateView):
    template_name = "search_results.html"

    def get_nyuuryoku(request):

        keyword = request.GET.get("keyword")
        brand = request.GET.get("brand")
        value = request.GET.get("value")
        display = request.GET.get("display")

        return keyword,brand,value,display
        

class ReviewEditView(generic.TemplateView):
    model = Review
    template_name = 'review_edit.html'
    form_class = ReviewForm
    # success_url = reverse_lazy('prefectures:prefectures_list')

    def form_valid(self, form):
        review = form.save(commit=False)
        review.userID = self.request.user
        review.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)