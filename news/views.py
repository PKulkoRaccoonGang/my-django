from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import NewsForm
from .models import News, Category


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home page'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


# def index(request):
#     news = News.objects.order_by('-created_at')
#     context = {
#         'news': news,
#         'title': 'News list',
#     }
#     return render(request, 'news/index.html', context)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/news_category.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category,
#     }
#     return render(request, 'news/category.html', context)

class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'


# def view_news(request, news_id):
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', context={'news_item': news_item})

class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')


#
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', context={'form': form})
