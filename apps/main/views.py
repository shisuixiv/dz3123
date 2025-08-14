from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Library,Book
from .serializers import LibrarySerializer,BookSerializer


class LibraryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        library = Library.objects.all()
        serializer = LibrarySerializer(library, many=True)
        return Response(serializer.data) 
    
class LibraryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class LibraryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

# Book
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer