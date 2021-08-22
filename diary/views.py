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
