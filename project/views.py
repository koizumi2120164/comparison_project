import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
<<<<<<< HEAD
from django.shortcuts import get_object_or_404

from .forms import InquiryForm, DiaryCreateForm
from .models import project

logger = logging.getLogger(__name__)
=======
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404

>>>>>>> d9fd165d7acb684f66cbd6d75ea934ac480f78cc


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # URLに埋め込まれた主キーから日記データを1件取得。取得できなかった場合は404エラー
<<<<<<< HEAD
        project = get_object_or_404(project, pk=self.kwargs['pk'])
        # ログインユーザーと日記の作成ユーザーを比較し、異なればraise_exceptionの設定に従う
        return self.request.user == project.user
=======
        prefectures = get_object_or_404(Prefectures, pk=self.kwargs['pk'])
        # ログインユーザーと日記の作成ユーザーを比較し、異なればraise_exceptionの設定に従う
        return self.request.user == prefectures.user
>>>>>>> d9fd165d7acb684f66cbd6d75ea934ac480f78cc


class IndexView(generic.TemplateView):
    template_name = "index.html"


<<<<<<< HEAD
class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('project:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)
=======
class SearchAdvancedView(generic.TemplateView):
    template_name = "search.html"
>>>>>>> d9fd165d7acb684f66cbd6d75ea934ac480f78cc


class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = project
    template_name = 'project_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = project.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries


<<<<<<< HEAD
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
        
=======
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
>>>>>>> d9fd165d7acb684f66cbd6d75ea934ac480f78cc
