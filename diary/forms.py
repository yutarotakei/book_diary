from django import forms

from .models import Book

CHOICES = [('1', '新書'),
           ('2', '文庫')]


class BookCreateForm(forms.ModelForm):
    genre = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'type')
