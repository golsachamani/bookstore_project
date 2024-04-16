from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Book
from . forms import BookForm
# Create your views here.
class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detai.html'

class BookCreatView(generic.CreateView):
    form_class = BookForm
    template_name = 'books/book_creat.html'
    context_object_name = 'form'

class BookUpdateView(generic.UpdateView):
    model = Book
    form_class =BookForm
    template_name = 'books/book_update.html'
    context_object_name = 'form'

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')