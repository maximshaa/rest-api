from rest_framework import generics, permissions, filters
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer, AuthorDetailSerializer


class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: Возвращает список всех книг.
    POST: Позволяет добавить новую книгу (только для администраторов).
    Реализована возможность поиска по полям: title, genre, author__name.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre', 'author__name']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Получение данных конкретной книги.
    PUT/PATCH/DELETE: Доступно только администраторам.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class AuthorListView(generics.ListAPIView):
    """
    GET: Получение списка всех авторов.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]


class AuthorRetrieveView(generics.RetrieveAPIView):
    """
    GET: Получение детальной информации об авторе,
    включая список его книг.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
    permission_classes = [permissions.AllowAny]
