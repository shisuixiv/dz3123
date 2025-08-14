from django.urls import path
from .views import (
    LibraryListCreateAPIView, LibraryRetrieveUpdateDestroyAPIView,
    BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    
    path('libraries/', LibraryListCreateAPIView.as_view(), name='library-list'),
    path('libraries/<int:pk>/', LibraryRetrieveUpdateDestroyAPIView.as_view(), name='library-detail'),
    
    
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
]
