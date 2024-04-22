from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Book
from . forms import BookForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'

# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detai.html'
@login_required
def book_detail_view(request, pk):
    #get book object
    book = get_object_or_404(Book, pk=pk)
    #get book comment
    book_comments = book.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment= comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
        
    else:
        comment_form = CommentForm()


    return render(request, 'books/book_detai.html',{'book':book, 'comments':book_comments,'comment_form': comment_form} )

class BookCreatView(LoginRequiredMixin,generic.CreateView):
    form_class = BookForm
    template_name = 'books/book_creat.html'
    context_object_name = 'form'

class BookUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Book
    form_class =BookForm
    template_name = 'books/book_update.html'
    context_object_name = 'form'

class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')