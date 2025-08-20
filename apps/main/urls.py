from django.urls import path
from .views import LibraryAPIView, BookAPIView, BookCreateAPIView, BookRetrieveAPIView, BookUpdateAPIView, BookDeleteAPIView
from .views import AuthorSerilizer,AuthorAPIView,AuthorDeleteAPIView,AuthorUpdateAPIView,AuthorDetailSerilizer,AuthorCreateAPIView,AuthorRetrieveAPIView

urlpatterns = [
    path("list-library/", LibraryAPIView.as_view(), name='list-library'),
    path("book-list/", BookAPIView.as_view(), name='book-list'),
    path("book-create/", BookCreateAPIView.as_view(), name='book-create'),
    path("book-detail/<int:pk>/", BookRetrieveAPIView.as_view(), name='detail-book'),
    path("book-update/<int:pk>/", BookUpdateAPIView.as_view(), name='book-update'),
    path("book-delete/<int:pk>/", BookDeleteAPIView.as_view(), name='book-delete'),
    path("author-list/", AuthorAPIView.as_view(), name='author-list'),
    path("author-create/", AuthorCreateAPIView.as_view(), name='author-create'),
    path("author-detail/<int:pk>/", AuthorRetrieveAPIView.as_view(), name='author-detail'),
    path("author-update/<int:pk>/", AuthorUpdateAPIView.as_view(), name='author-update'),
    path("author-delete/<int:pk>/", AuthorDeleteAPIView.as_view(), name='author-delete'),
]