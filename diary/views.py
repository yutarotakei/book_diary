from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book
from .forms import BookCreateForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

import matplotlib

# バックエンドを指定
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
from django.http import HttpResponse


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'book_list.html'

    def get_queryset(self):
        books = Book.objects.filter(user=self.request.user).order_by('-read_at')
        return books


class BookCreateView(generic.FormView):
    template_name = 'book_create.html'
    form_class = BookCreateForm


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('diary:book_list')


def bookcreate(request, *args, **kwargs):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        genre = request.POST['genre']
        type = request.POST['type']

        dict = {'1': '新書', '2': '文庫', '3': '技術書', '4': '専門書', '5': '単行本'}
        genre = dict[genre]

        book = Book()
        book.title = title
        book.author = author
        book.genre = genre
        book.type = type
        book.user_id = request.user.id
        book.save()
        return redirect(to='/book-list')
    else:
        form = BookCreateForm
    return render(request, 'book_create.html', {'form': form})


# SVG化
def plt2svg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s


# 実行するビュー関数
def get_svg(request):
    y = []
    for i in range(1, 13):
        m1 = Book.objects.filter(user=request.user).filter(read_at__year='2021', read_at__month='{}'.format(i)).count()
        y.append(m1)
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    plt.rcParams["figure.figsize"] = (8, 6)
    plt.bar(x, y, color='#00d5ff')
    plt.title("the number of books you read")
    plt.xlabel("Month")
    plt.ylabel("book")
    svg = plt2svg()  # SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response
