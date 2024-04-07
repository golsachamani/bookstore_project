from django.shortcuts import render
from django.views import generic
from .models import Book
# Create your views here.
class BookListView(generic.ListView):
    form = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'