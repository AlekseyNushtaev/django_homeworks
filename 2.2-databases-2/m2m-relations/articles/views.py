from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    # template = 'articles/news.html'
    # context = {'object_list': Article.objects.all()}
    # ordering = '-published_at'
    # return render(request, template, context)
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.order_by(ordering).prefetch_related('scopes')
    context = {
        'object_list': articles,
    }

    return render(request, template, context)