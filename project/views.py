import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Review, Recently_viewed, Wishlist
from django.shortcuts import redirect
from shop.models import *
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from . forms import *

logger = logging.getLogger(__name__)


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class IndexView(generic.TemplateView):
    template_name = "index.html"


"""
    def get_queryset(self):
        ranking = Product.objects.order_by('-like_product')[0:10]
        return ranking

    def get_queryset(self):
        word = Word.objects.order_by('-updated_at')[0:10]
        return word
"""
    

class SearchAdvancedView(generic.TemplateView):
    template_name = 'search_advanced.html'

class ProductListView(generic.ListView):
    model = Product, Category
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')
        product = get_object_or_404(Product, id=pk,slug=slug)
        return product
        
    def categories(request):
        return {
            'categories': Category.objects.all()
        }

    def product_all(request):
        products = Product.objects.all()
        return render(request, 'shop/product_list.html', {'products': products})

    def category_list(request, category_slug=None):
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        return render(request, 'shop/category.html', {'category': category, 'products':products})

class ProductDetailView(generic.DetailView):
    template_name = 'shop/product_detail.html'
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')
        product = get_object_or_404(Product, id=pk,slug=slug)
        return product

    queryset = Product.objects.all()
    context_object_name = 'product'
    success_url = reverse_lazy('project:product_list')

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
            if value == "???500???":
                product = Product.objects.filter(Q(product_name__contains=keyword) | Q(price1_lt=500) | Q(price2_lt=500) | Q(price3_lt=500))
            elif value == "500??????1000???":
                product = Product.objects.filter(Q(product_name__contains=keyword) | Q(price1_gte=500) & Q(price1_lt=1000) | Q(price2_gte=500) & Q(price2_lt=1000) | Q(price3_gte=500) & Q(price3_lt=1000))
            elif value == "1000??????5000???":
                product = Product.objects.filter(Q(product_name__contains=keyword) | Q(price1_gte=1000) & Q(price1_lt=5000) | Q(price2_gte=1000) & Q(price2_lt=5000) | Q(price3_gte=1000) & Q(price3_lt=5000))
            elif value == "5000??????10000???":
                product = Product.objects.filter(Q(product_name__contains=keyword) | Q(price1_gte=5000) & Q(price1_lt=10000) | Q(price2_gte=5000) & Q(price2_lt=10000) | Q(price3_gte=5000) & Q(price3_lt=10000))
            elif value == "10000??????":
                product = Product.objects.filter(Q(product_name__contains=keyword) | Q(price1_gt=10000) | Q(price2_gt=10000) | Q(price3_gt=10000))
            else:
                product = Product.objects.filter(Q(product_name__contains=keyword))

            return product


        if brand == "amazon" or brand == "??????" or brand == "Yahoo":
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
        
        return product


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
        messages.success(self.request, '??????????????????????????????')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "???????????????????????????????????????")
        return super().form_invalid(form)


class DiaryUpdateView(LoginRequiredMixin, OnlyYouMixin, generic.UpdateView):
    model = project
    template_name = 'project_update.html'
    form_class = projectCreateForm

    def get_success_url(self):
        return reverse_lazy('project:project_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '??????????????????????????????')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "???????????????????????????????????????")
        return super().form_invalid(form)


class DiaryDeleteView(LoginRequiredMixin, OnlyYouMixin, generic.DeleteView):
    model = project
    template_name = 'project_delete.html'
    success_url = reverse_lazy('project:project_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "??????????????????????????????")
        return super().delete(request, *args, **kwargs)
        return keyword,brand,value,display
"""


class ReviewView(LoginRequiredMixin, OnlyYouMixin, generic.DetailView):
    model = Review
    template_name = 'review.html'


class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
    model = Review
    template_name = 'review_create.html'
    form_class = ReviewForm
    # success_url = reverse_lazy('project:item')
    # ???????????????????????????????????????

    def form_valid(self, form):
        review = form.save(commit=False)
        review.userID = self.request.user
        review.save()
        messages.success(self.request, '????????????????????????????????????')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "?????????????????????????????????????????????")
        return super().form_invalid(form)
        

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
        messages.success(self.request, '????????????????????????????????????')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "?????????????????????????????????????????????")
        return super().form_invalid(form)


class ReviewDeleteView(LoginRequiredMixin, OnlyYouMixin, generic.DeleteView):
    model = Review
    template_name = 'review_delete.html'
    success_url = reverse_lazy('project:review_delete')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "????????????????????????")
        return super().delete(request, *args, **kwargs)


"""
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
        return account"""


class ProductAllView(generic.ListView):
    model = Product
    template_name = 'product_all.html'
    paginate_by = 3

    def get_queryset(self):
        product_all = Product.objects.order_by('-created_at')
        return product_all

    def get_queryset(self):
        ranking = Product.objects.order_by('-like_product')[0:10]
        return ranking



class ItemView(generic.DetailView):
    model = Product
    template_name = 'item.html'
    form_class = ItemForm

    def recently(self,*args, **kwargs):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Product, pk=post_pk)
        recently = Recently_viewed(userID=self.request.user, productID=post)
        recently.save()

    #??????????????????????????????
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        # ??????????????????????????????????????????????????????????????????
        if Wishlist.objects.filter(userID=self.request.user).exists():
            context['like'] = True
        else:
            context['like'] = False
        
        return context



"""def like_for_post(self, request, *args, **kwargs):
    post_pk = self.kwargs['pk']

    context = {
        'user': f'{request.user.last_name} {request.user.first_name}',
    }
    
    post = get_object_or_404(Product, pk=post_pk)
    like = Wishlist.objects.filter(wish_item=post, userID=request.user)

    if like.exists():
        like.delete()
        context['method'] = 'delete'

    else:
        like.create(wish_item=post, userID=request.user)
        context['method'] = 'create'

    context['like_for_post_count'] = post.likeforpost_set.count()

    return JsonResponse(context)    


"""
class RecentlyViewedView(LoginRequiredMixin, generic.ListView):
    model = Recently_viewed
    template_name = 'recently_viewed.html'
    paginate_by = 6

    def get_queryset(self):
        recently_viewd = []
        recently = Recently_viewed.objects.filter(userID=self.request.user.id).order_by('-last_visited')
        for product in recently:
            recently_product = Product.objects.filter(productID=product.productID)
            recently_viewd += recently_product
        return recently_viewd
        
        
class RankListView(generic.ListView):
    model = Product
    template_name = 'rank_list.html'
    paginate_by = 3

    def get_queryset(self):
        ranking = Product.objects.order_by('-like_product')
        return ranking
        
        

class WishListView(LoginRequiredMixin, generic.ListView):
    model = Wishlist
    template_name = 'wish_list.html'
    paginate_by = 2

    def get_queryset(self):
        wish_product = []
        wish = Wishlist.objects.filter(userID=self.request.user.id).order_by('-added_date')
        for wished_item in wish:
            product = Product.objects.filter(slug=wished_item.slug)
            wish_product += product
        
        return wish_product
        

"""?????????????????????   
class WishDeleteView(LoginRequiredMixin, OnlyYouMixin, generic.DeleteView):
    model = Wishlist
    template_name = 'wish_delete.html'
    success_url = reverse_lazy('project:wish_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "???????????????????????????????????????????????????")
        return super().delete(request, *args, **kwargs)"""


class ProfileEditView(LoginRequiredMixin, OnlyYouMixin, generic.DeleteView):
    model = CustomUser
    template_name = "profile_edit.html"


class ProfileUpdateView(LoginRequiredMixin, OnlyYouMixin, generic.UpdateView):
    model = CustomUser
    template_name = "profile_update.html"
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse_lazy('project:profile_edit', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '?????????????????????????????????')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "???????????????????????????????????????")
        return super().form_invalid(form)