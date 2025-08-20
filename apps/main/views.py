from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import Library, Book,Author
from .serializers import LibrarySerilizer, BookSerializer, BookDetailSerializer,AuthorSerilizer,AuthorDetailSerilizer


class LibraryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        library = Library.objects.all()
        serializer = LibrarySerilizer(library, many=True)
        return Response(serializer.data)    
    
@method_decorator(cache_page(60), name='dispatch')
class AuthorAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = AuthorSerilizer

@method_decorator(cache_page(60), name='dispatch')
class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#end

class AuthorCreateAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerilizer

class AuthorRetrieveAPIView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerilizer

class AuthorUpdateAPIView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerilizer

class AuthorDeleteAPIView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerilizer