from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book
from .forms import BookCreateForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy


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


def bookcreate(request, *args, **kwargs):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        genre = request.POST['genre']
        type = request.POST['type']

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
