import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Review, Recently_viewed, Wishlist
from shop.models import *
from django.shortcuts import render, get_object_or_404
from . forms import *
from django.shortcuts import redirect
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from django.http import JsonResponse
from django.core.paginator import Paginator

logger = logging.getLogger(__name__)


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser
    

# トップページ
class IndexView(generic.ListView):
    model = Product
    template_name = "index.html"
    context_object_name = 'user_review_list'

    # ランキング、新着口コミ情報を取り出す
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'product_list': Product.objects.all().annotate(Count('like_product')).order_by('-like_product__count', '-created_at'),
            'word_list': Word.objects.order_by('-created_at'),

        })

        return context


class SearchAdvancedView(generic.TemplateView):
    template_name = 'search_advanced.html'

class ProductListView(generic.ListView):
    model = Product, Category
    
    def categories(request):
        return {
            'categories': Category.objects.all()
        }

    def product_all(request):
        products = Product.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(products, 9)
        page_object = paginator.get_page(page)
        page_object.adjusted_elided_pages = paginator.get_elided_page_range(page)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context = {
            'products': products, 
            "page_obj": page_object
        }
        return render(request, 'product_list.html', context)

    def category_list(request, category_slug=None):
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        page = request.GET.get('page', 1)
        paginator = Paginator(products, 6)
        page_range = paginator.get_elided_page_range(number=page)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context = {
            'products': products,
            'category': category, 
        }
        return render(request, 'category.html', context)



# 商品詳細ページ
class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        review = Review.objects.filter(productID=product.pk).order_by('-created_at')
        user = CustomUser.objects.filter(username=self.request.user)

        if user:
            wish = Wishlist.objects.filter(userID=self.request.user, wished_item=product.pk)
        else:
            wish = None

        context.update({
            'product_list': product,
            'review_list' : review,
            'wish_list' : wish,
            'like_for_post_count' : product.like_product.count()
        })

        return context
    

# 商品のいいね機能
def Ajax_ch_product(request, slug):
    """Ajax処理"""
    user = request.user
    context = {
        'user_id': f'{ request.user }',
    }

    product = Product.objects.get(slug=slug)
    wish_list = Wishlist.objects.filter(wished_item=product)
    like = False

    for wish in wish_list:
        if wish.userID == user:
            like = True

    if like == True:
        wish.delete()
        context['method'] = 'delete'
        product.like_product.remove(user)
    else:
        wish_list.create(userID=user, wished_item=product)
        context['method'] = 'create'
        product.like_product.add(user)

    context['like_for_post_count'] = product.like_product.count()
 
    return JsonResponse(context)


# 検索結果ページ
def get_queryset(request):
    # Sessionから条件取得
    params = request.session.get('params')

    if not params or request.GET.get("keyword"):
        # Sessionに値がないか、新しくキーワードから値を取得した場合、GETから取得
        params = {
            "keyword" : request.GET.get("keyword"),
            "value" : request.GET.get("value"),
            "display" : request.GET.get("display")
        }

    # Sessionに保存
    request.session['params'] = params

    if params['display'] == "popular":
        if params['value']:
            product =  Product.objects.filter(
                product_name__contains=params['keyword'],
                price1__lte=params['value']
                ).annotate(Count('like_product')).order_by('-like_product__count', '-created_at')
        else:
            product =  Product.objects.filter(
                product_name__contains=params['keyword'],
                ).annotate(Count('like_product')).order_by('-like_product__count', '-created_at')
    
    else:
        if params['value']:
            product =  Product.objects.filter(
                product_name__contains=params['keyword'],
                price1__lte=params['value']
                ).order_by('-created_at')
        else:
            product =  Product.objects.filter(
                product_name__contains=params['keyword']
                ).order_by('-created_at')
            
    # paginate_byの実装
    # 1ページに表示させる数を指定する
    count = 5

    # pagenateの実行
    paginator = Paginator(product, count)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request,'search_results.html',context={'object_list':page_obj.object_list,'page_obj': page_obj})


# 口コミ詳細ページ
class WordDetailView(generic.DetailView):
    model = Word
    template_name = 'worddetail.html'


# 口コミのいいね機能
def Ajax_ch_word(request, pk):
    """Ajax処理"""
    user = request.user
    context = {
        'user_id': f'{ request.user }',
    }
    word = get_object_or_404(Word, pk=pk)
    like = False

    for like in word.like_word.all():
        if like == user:
            like = True

    if like == True:
        word.like_word.remove(user)
        context['method'] = 'delete'
    else:
        word.like_word.add(user)
        context['method'] = 'create'
 
    return JsonResponse(context)


# 口コミ情報の更新
class WordUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Word
    template_name = 'wordpost.html'
    form_class = WordCreateForm

    def get_success_url(self):
        return reverse_lazy('project:word_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '口コミを更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "口コミの更新に失敗しました。")
        return super().form_invalid(form)


# 口コミ削除ページ
class WordDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Word
    template_name = 'word_delete.html'
    success_url = reverse_lazy('project:wordreiew_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "口コミを削除しました。")
        # アカウントテーブルの口コミ数を削除した状態で登録
        target_data = Word.objects.filter(created_by=self.request.user).count()
        user = CustomUser.objects.filter(username=self.request.user)
        for customuser in user:
            customuser.no_of_word = target_data
        customuser.save()
        return super().delete(request, *args, **kwargs)


# 口コミ掲示板一覧ページ
class WordReiewListView(generic.ListView):
    model = Word
    template_name = 'wordreiew_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Word.objects.order_by('-created_at')


# 口コミ掲示板(人気順)一覧ページ。ログイン中のユーザーのみ可能。
class WordReiewList_LikeView(LoginRequiredMixin,generic.ListView):
    model = Word
    template_name = 'wordreiew_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Word.objects.all().annotate(Count('like_word')).order_by('-like_word__count', '-created_at')



# 口コミ作成ページ
class WordCreateView(LoginRequiredMixin,generic.CreateView):
    model = Word
    template_name = 'wordpost.html'
    form_class = WordCreateForm
    success_url = reverse_lazy('project:wordreiew_list')

    def form_valid(self, form):
        # 口コミを登録
        word = form.save(commit=False)
        word.created_by = self.request.user
        word.save()
        # アカウントテーブルの口コミ数を登録
        target_data = Word.objects.filter(created_by=self.request.user).count()
        user = CustomUser.objects.filter(username=self.request.user)
        for customuser in user:
            customuser.no_of_word = target_data
        customuser.save()
        messages.success(self.request, '口コミを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "口コミの作成に失敗しました。")
        return super().form_invalid(form)
       


# レビューの詳細ページ
class ReviewView(generic.DetailView):
    model = Review
    template_name = 'review.html'


# レビューのいいね機能
def Ajax_ch_review(request, pk):
    """Ajax処理"""
    user = request.user
    context = {
        'user_id': f'{ request.user }',
    }
    review = get_object_or_404(Review, pk=pk)
    like = False

    for like in review.like_review.all():
        if like == user:
            like = True

    if like == True:
        review.like_review.remove(user)
        context['method'] = 'delete'
    else:
        review.like_review.add(user)
        context['method'] = 'create'
 
    return JsonResponse(context)


# レビュー作成ページ
class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
    model = Review
    template_name = 'review_create.html'
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('project:product_detail', kwargs={"slug": self.kwargs['slug']})

    def form_valid(self, form):
        # 作成したレビューの情報を登録   
        review = form.save(commit=False)
        review.created_by = self.request.user
        product = Product.objects.get(slug=self.kwargs['slug'])
        review.productID = product
        review.save()
        # アカウントテーブルのレビュー数を登録
        target_data = Review.objects.filter(created_by=self.request.user).count()
        user = CustomUser.objects.filter(username=self.request.user)
        for customuser in user:
            customuser.no_of_review = target_data
        customuser.save()
        messages.success(self.request, 'レビューを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "レビューの作成に失敗しました。")
        return super().form_invalid(form)
        

# レビュー編集ページ
class ReviewEditView(LoginRequiredMixin, generic.UpdateView):
    model = Review
    template_name = 'review_edit.html'
    form_class = ReviewForm

    def get_success_url(self):
        return reverse_lazy('project:review', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        review = form.save(commit=False)
        review.created_by = self.request.user
        review_list = Review.objects.get(pk=self.kwargs['pk'])
        product = Product.objects.get(pk=review_list.productID.pk)
        review.productID = product
        review.save()
        messages.success(self.request, 'レビューを編集しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "レビューの編集に失敗しました。")
        return super().form_invalid(form)


# レビュー削除
class ReviewDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Review
    template_name = 'review_delete.html'

    def get_success_url(self):
        review = Review.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy('project:product_detail', kwargs={'slug': review.productID.slug})

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "レビューを削除しました。")
        # 削除後のアカウントテーブルのレビュー数を登録
        target_data = Review.objects.filter(created_by=self.request.user).count()
        user = CustomUser.objects.filter(username=self.request.user)
        for customuser in user:
            customuser.no_of_review = target_data
        customuser.save()
        return super().delete(request, *args, **kwargs)


# ユーザーページ
class UserReviewPageView(generic.ListView):
    model = CustomUser
    template_name = 'user_review_page.html'
    context_object_name = 'user_review_list'

    # アカウント、口コミ、レビュー情報を取得
    def get_context_data(self, **kwargs):
        context = super(UserReviewPageView, self).get_context_data(**kwargs)
        review_list = Review.objects.filter(created_by=self.kwargs['pk']).order_by('-created_at')
        word_list = Word.objects.filter(created_by=self.kwargs['pk']).order_by('-created_at')
        if word_list:
            for user in word_list:
                user_list = CustomUser.objects.filter(username=user.created_by)
        elif review_list:
            for user in review_list:
                user_list = CustomUser.objects.filter(username=user.created_by)
        else:
            user_list = CustomUser.objects.filter(username=self.request.user)

        context.update({
            'review_list': review_list,
            'word_list': word_list,
            'user_list': user_list
        })
        return context
    

# 選択したユーザーが投稿したレビューリスト
class ReviewListView(generic.ListView):
    model = Review
    template_name = 'review_list.html'
    paginate_by = 5

    def get_queryset(self):
        review_list = Review.objects.filter(created_by=self.kwargs['pk']).order_by('-created_at')
        return review_list
    

# 選択したユーザーが投稿した口コミリスト
class WordListView(generic.ListView):
    model = Word
    template_name = 'word_list.html'
    paginate_by = 5

    def get_queryset(self):
        word_list = Word.objects.filter(created_by=self.kwargs['pk']).order_by('-created_at')
        return word_list



# 閲覧履歴ページ
class RecentlyViewedView(LoginRequiredMixin, generic.ListView):
    model = Recently_viewed
    template_name = 'recently_viewed.html'
    paginate_by = 6

    def get_queryset(self):
        recently_list = Recently_viewed.objects.filter(userID=self.request.user).order_by('-last_visited')
        return recently_list
        

# ランキングページ       
class RankListView(generic.ListView):
    model = Product
    template_name = 'rank_list.html'
    paginate_by = 10

    def get_queryset(self):
        ranking = Product.objects.all().annotate(Count('like_product')).order_by('-like_product__count', '-created_at')
        return ranking
        
        
# ログインしているユーザがお気に入りした商品の一覧ページ
class WishListView(LoginRequiredMixin, generic.ListView):
    model = Wishlist
    template_name = 'wish_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        wish_list = Wishlist.objects.filter(userID=self.request.user).order_by('-added_date')
        product_list = []

        if wish_list:
            for product in wish_list:
                product_list += Product.objects.filter(product_name=product.wished_item)

        return product_list
        

# 自分のアカウント情報の詳細ページ
class ProfileEditView(LoginRequiredMixin, OnlyYouMixin, generic.DeleteView):
    model = CustomUser
    template_name = "profile_edit.html"


# アカウント情報の更新
class ProfileUpdateView(LoginRequiredMixin, OnlyYouMixin, generic.UpdateView):
    model = CustomUser
    template_name = "profile_update.html"
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse_lazy('project:profile_edit', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '情報は保存されました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "情報の保存に失敗しました。")
        return super().form_invalid(form)
    

# 商品のレビュー一覧
class ReviewProductView(generic.ListView):
    model = Review
    template_name = 'review_product.html'
    paginate_by = 5

    def get_queryset(self):
        product = Product.objects.get(slug=self.kwargs['slug'])
        review_list = Review.objects.filter(productID=product).order_by('-created_at')
        return review_list