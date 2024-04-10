from django.forms import ModelForm, TextInput, Textarea, NumberInput
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'text', 'published', 'count']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть автора'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть опис'
            }),
            'published': TextInput(attrs={
                'class': 'col-xs-4',
                'id': 'ex1',
                'placeholder': 'Введіть рік видання'
            }),
            'count': NumberInput(attrs={
                'class': 'col-xs-2',
                'id': 'ex2',
                'placeholder': 'Введіть кількість книжок'
            }),
        }