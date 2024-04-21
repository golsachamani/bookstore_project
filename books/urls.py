from django.urls import path
from .views import *

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/',book_detail_view, name='book_detai' ),
    path('creat/', BookCreatView.as_view(), name='book_creat' ),
    path('<int:pk>/update/', BookUpdateView.as_view(), name= 'book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name= 'book_delete')
]