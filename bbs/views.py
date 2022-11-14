from django.views import generic
from .models import Post, LikeForPost
from django.http import JsonResponse  # 追加
from django.shortcuts import get_object_or_404  # 追加
from . forms import CreateForm
from django.urls import reverse_lazy
from django.contrib import messages


class PostList(generic.ListView):
    template_name = 'bbs/post_list.html'
    model = Post


class PostDetail(generic.DetailView):
    template_name = 'bbs/post_detail.html'
    model = Post


    def get_context_data(self, request, *args, **kwargs):
        post_pk = request.POST.get('post_pk')
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, pk=post_pk)
        like_for_post_count = LikeForPost.objects.filter(target=post).count()
        # ポストに対するイイね数
        context['like_for_post_count'] = like_for_post_count
        # ログイン中のユーザーがイイねしているかどうか
        if LikeForPost.objects.filter(user=self.request.user).exists():
            context['is_user_liked_for_post'] = True
        else:
            context['is_user_liked_for_post'] = False
        

        return context


def like_for_post(request):
    post_pk = request.POST.get('post_pk')
    context = {
        'user': f'{request.user.last_name} {request.user.first_name}',
    }
    post = get_object_or_404(Post, pk=post_pk)
    like = LikeForPost.objects.filter(target=post, user=request.user)

    if like.exists():
        like.delete()
        context['method'] = 'delete'
    else:
        like.create(target=post, user=request.user)
        context['method'] = 'create'

    context['like_for_post_count'] = post.likeforpost_set.count()

    return JsonResponse(context)

class CreateView(generic.CreateView):
    model = Post
    template_name = 'bbs/create.html'
    form_class = CreateForm
    success_url = reverse_lazy('bbs:post_list')

    def form_valid(self, form):
        prefectures = form.save(commit=False)
        prefectures.user = self.request.user
        prefectures.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)