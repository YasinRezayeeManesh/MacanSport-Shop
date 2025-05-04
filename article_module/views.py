from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from account_module.models import User
from .models import Article, ArticleComment

from about_us_module.models import ManyInfo


# Create your views here.


class ArticleListView(ListView):
    template_name = 'article_module/article_list.html'
    context_object_name = 'articles'
    model = Article
    paginate_by = 4


class ArticleDetailView(DetailView):
    template_name = 'article_module/article_detail.html'
    context_object_name = 'article'
    model = Article
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article: Article = kwargs.get('object')
        context['comments'] = ArticleComment.objects.filter(article_id=article.id, parent=None, success=True).order_by('-shamsi_date').prefetch_related('articlecomment_set')
        return context


def send_article_comment(request):
    if request.user.is_authenticated:
        article_comment = request.GET.get('articleComment')
        article_id = request.GET.get('articleId')
        parent_id = request.GET.get('parentId')
        new_comment = ArticleComment(comment=article_comment, article_id=article_id, parent_id=parent_id,
                                     user_id=request.user.id)
        new_comment.save()
        return HttpResponse('success')
