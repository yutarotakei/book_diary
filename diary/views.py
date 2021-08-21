from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book
from .forms import BookCreateForm
from django.urls import reverse_lazy


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'book_list.html'

    def get_queryset(self):
        books = Book.objects.filter(user=self.request.user).order_by('-read_at')
        return books


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    template_name = 'book_create.html'
    form_class = BookCreateForm
    success_url = reverse_lazy('diary:book_list')

    def form_valid(self, form):
        book = form.save(commit=False)
        book.user = self.request.user
        book.save()
        return super().form_valid(form)
