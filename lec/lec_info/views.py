from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.shortcuts import redirect
from django.contrib import messages
from .forms import CommentForm
from .models import Comment

class CommentIndexView(ListView):
    model = Comment
    queryset = Comment.objects.order_by('-updated_time')
    paginate_by = 2

class CommentDetailView(DetailView):
    model = Comment

class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('lec_info:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'コメント投稿'
        context['form_name'] = 'コメント投稿'
        context['button_label'] = '新規投稿する'
        return context

    def form_valid(self, form):
        self.object = comment = form.save()
        messages.success(self.request, "コメントを投稿しました")
        return redirect(self.get_success_url())


class UpdateCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('lec_info:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'コメント更新'
        context['form_name'] = 'コメント更新'
        context['button_label'] = '更新する'
        return context

    def form_valid(self, form):
        self.object = comment = form.save()
        message.redirect(self.request, "コメントを更新しました")
        return redirect(self.get_success_url())

class DeleteCommentView(DeleteView):
    model = Comment
    success_url = reverse_lazy('lec_info:index')

    def delete(self, request, *args, **kwargs):
        self.object = comment = self.get_object()
        comment.delete()
        message.success(self,request, "コメントを削除しました")
        return redirect(self.get_success_url())
