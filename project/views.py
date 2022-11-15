import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Word
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import HttpResponse

logger = logging.getLogger(__name__)


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # URLに埋め込まれた主キーから日記データを1件取得。取得できなかった場合は404エラー
        project = get_object_or_404(project, pk=self.kwargs['pk'])
        # ログインユーザーと日記の作成ユーザーを比較し、異なればraise_exceptionの設定に従う
        return self.request.user == project.user


class IndexView(generic.TemplateView):
    template_name = "index.html"
    

class SearchAdvancedView(generic.TemplateView):
    template_name = 'search_advanced.html'


"""検索結果
class SearchResultsView(generic.TemplateView):
    template_name = "search_results.html"
    model = Product
    paginate_by = 3


    def get_queryset(self, request):
        keyword = request.GET.get("keyword")
        brand = request.GET.get("brand")
        value = request.GET.get("value")
        display = request.GET.get("display")

        def Value():
            if value == "～500円":
                product = Product.objects.filter(Q(product_name__contains=keyword) | Q(price1_lt=500) | Q(price2_lt=500) | Q(price3_lt=500))
            elif value == "500円～1000円":
                product = Product.objects.filter(Q(product_name__contains=keyword) | Q(price1_gte=500) & Q(price1_lt=1000) | Q(price2_gte=500) & Q(price2_lt=1000) | Q(price3_gte=500) & Q(price3_lt=1000))
            elif value == "1000円～5000円":
                product = Product.objects.filter(Q(product_name__contains=keyword) | Q(price1_gte=1000) & Q(price1_lt=5000) | Q(price2_gte=1000) & Q(price2_lt=5000) | Q(price3_gte=1000) & Q(price3_lt=5000))
            elif value == "5000円～10000円":
                product = Product.objects.filter(Q(product_name__contains=keyword) | Q(price1_gte=5000) & Q(price1_lt=10000) | Q(price2_gte=5000) & Q(price2_lt=10000) | Q(price3_gte=5000) & Q(price3_lt=10000))
            elif value == "10000円～":
                product = Product.objects.filter(Q(product_name__contains=keyword) | Q(price1_gt=10000) | Q(price2_gt=10000) | Q(price3_gt=10000))
            else:
                product = Product.objects.filter(Q(product_name__contains=keyword))


        if brand == "amazon" or brand == "楽天" or brand == "Yahoo":
            if display == "popular":
                Value()
                product |=  Q(product_brand_exact=brand)
                product = Product.object.order_by('like_product').reverse()
            else:
                Value()
                product |=  Q(product_brand_exact=brand)
                product = Product.object.order_by('productID').reverse()

        else:
            if display == "popular":
                Value()
                product = Product.object.order_by('like_product').reverse()

            else:
                Value()
                product = Product.object.order_by('productID').reverse()
        
        return product"""


"""

class DiaryDetailView(LoginRequiredMixin, OnlyYouMixin, generic.DetailView):
    model = project
    template_name = 'diary_detail.html'


class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = project
    template_name = 'diary_create.html'
    form_class = projectCreateForm
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)


class DiaryUpdateView(LoginRequiredMixin, OnlyYouMixin, generic.UpdateView):
    model = project
    template_name = 'project_update.html'
    form_class = projectCreateForm

    def get_success_url(self):
        return reverse_lazy('project:project_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の更新に失敗しました。")
        return super().form_invalid(form)


class DiaryDeleteView(LoginRequiredMixin, OnlyYouMixin, generic.DeleteView):
    model = project
    template_name = 'project_delete.html'
    success_url = reverse_lazy('project:project_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request, *args, **kwargs)
        return keyword,brand,value,display
"""

"""
レビュー詳細ページ
class ReviewView(LoginRequiredMixin, OnlyYouMixin, generic.DetailView):
    model = Review
    template_name = 'review.html'


レビュー作成ページ
class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
    model = Review
    template_name = 'review_create.html'
    form_class = ReviewForm
    # success_url = reverse_lazy('prefectures:prefectures_list')
    # ↑商品詳細ページへ遷移する

    def form_valid(self, form):
        review = form.save(commit=False)
        review.userID = self.request.user
        review.save()
        messages.success(self.request, 'レビューを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "レビューの作成に失敗しました。")
        return super().form_invalid(form)
        

レビュー編集ページ
class ReviewEditView(LoginRequiredMixin, OnlyYouMixin, generic.UpdateView):
    model = Review
    template_name = 'review_edit.html'
    form_class = ReviewForm

    def get_success_url(self):
        return reverse_lazy('project:review_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        review = form.save(commit=False)
        review.userID = self.request.user
        review.save()
        messages.success(self.request, 'レビューを編集しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "レビューの編集に失敗しました。")
        return super().form_invalid(form)


レビュー削除ページ
class ReviewDeleteView(LoginRequiredMixin, OnlyYouMixin, generic.DeleteView):
    model = Review
    template_name = 'review_delete.html'
    # success_url = reverse_lazy('project:review_delete')
    # ↑商品詳細ページへ遷移する

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request, *args, **kwargs)


ユーザー詳細ページ
class UserReviewPageView(generic.ListView):
    model = Review
    template_name = 'user_review_page.html'

    def get_queryset(self):
        review = Review.objects.filter(created_by=self.request.user).order_by('-created_at')
        return review

    def get_queryset(self):
        word = Word.objects.filter(created_by=self.request.user).order_by('-created_at')
        return word

    def get_queryset(self):
        account = Word.objects.filter(created_by=self.request.user).order_by('-created_at')
        return account


商品一覧（新着順）ページ
class ProductAllView(generic.ListView):
    model = Product
    template_name = 'product_all.html'
    paginate_by = 3

    def get_queryset(self):
        product_all = Product.objects.order_by('-created_at')
        return product

    def get_queryset(self):
        ranking = Product.objects.order_by('-like_product')
        return ranking


商品詳細ページ
    class ItemView(generic.DetailView):
    model = Product
    template_name = 'item.html'
    form_class = ItemForm

    def recently(request):
        recently = Recently_viewed(userID=self.request.user, productID=product.productID)
        recently.save()
        return super().form_valid(form)


閲覧履歴
class RecentlyViewedView(LoginRequiredMixin, OnlyYouMixin, generic.ListView):
    model = Recently_viewed
    template_name = 'recently_viewed.html'
    paginate_by = 6

    def get_queryset(self):
        recently = Recently_viewed.objects.filter(user=self.request.user).order_by('-last_visited')
        product = Product.object.filter(productID=recently.productID)
        return recently, product
        
        
ランキング
class RankListView(generic.ListView):
    model = Product
    template_name = 'rank_list.html'
    paginate_by = 3

    def get_queryset(self):
        ranking = Product.objects.order_by('-like_product')
        return ranking
        
        
お気に入り
class WishListView(LoginRequiredMixin, OnlyYouMixin, generic.ListView)
    model = Wishlist
    template_name = 'wish_list.html'
    paginate_by = 2

    def get_queryset(self):
        wish = Wishlist.objects.filter(userID=self.request.user).order_by('-added_date')
        product = Product.object.filter(productID=wish.wished_item)
        return product, wish"""