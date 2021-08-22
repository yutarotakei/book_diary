from django import forms

from .models import Book

CHOICES = [('1', '新書'),
           ('2', '文庫'),
           ('3', '技術書'),
           ('4', '専門書'),
           ('5', '単行本')]



class BookCreateForm(forms.ModelForm):
    genre = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    type = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'純文学、現代批評など'
    }))

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'type')
