from django.views import generic
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404



class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # URLに埋め込まれた主キーから日記データを1件取得。取得できなかった場合は404エラー
        prefectures = get_object_or_404(Prefectures, pk=self.kwargs['pk'])
        # ログインユーザーと日記の作成ユーザーを比較し、異なればraise_exceptionの設定に従う
        return self.request.user == prefectures.user


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


class PrefecturesDetailView(LoginRequiredMixin, OnlyYouMixin, generic.DetailView):
    model = Review
    template_name = 'review.html'
        

class ReviewEditView(generic.TemplateView):
    model = Review
    template_name = 'review_edit.html'
    form_class = ReviewForm
    # success_url = reverse_lazy('prefectures:prefectures_list')

    def form_valid(self, form):
        review = form.save(commit=False)
        review.userID = self.request.user
        review.save()
        messages.success(self.request, 'レビューを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "レビューの作成に失敗しました。")
        return super().form_invalid(form)


class ReviewDeleteView(LoginRequiredMixin, OnlyYouMixin, generic.DeleteView):
    model = Review
    template_name = 'prefectures_delete.html'
    success_url = reverse_lazy('prefectures:prefectures_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request, *args, **kwargs)