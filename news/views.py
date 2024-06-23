from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewsForm
from .models import News, Category


def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'News list',
    }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, 'news/category.html', context)


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', context={'news_item': news_item})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', context={'form': form})
