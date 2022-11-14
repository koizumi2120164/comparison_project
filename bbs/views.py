from django.views import generic
from .models import Post, LikeForPost
from .forms import CreateForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


class PostList(generic.ListView):
    template_name = 'post_list.html'
    model = Post


class PostDetail(generic.DetailView):
    template_name = 'post_detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        like_for_post_count = self.object.likeforpost_set.count()
        # ポストに対するイイね数
        context['like_for_post_count'] = like_for_post_count

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
    template_name = 'create.html'
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