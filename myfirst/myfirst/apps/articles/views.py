from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect

from django.shortcuts import render
from .models import Article
from django.urls import reverse


def index(request):
    return HttpResponse('Hello, world!')


def test(request):
    return HttpResponse('Hello, world!')


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья НЕ найдена(((')
    latest_comment_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'articles/detail.html', {'article': a, 'latest_comment_list': latest_comment_list})

    # return render(request, 'articles/detail.html', {'article': a})



def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Articles is not exists')

    a.comment_set.create(author_name=request.POST['name'], coment_text = request.POST['text'])
    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))