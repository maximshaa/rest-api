from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """Сериализатор для базовой информации об авторе."""
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography']


class AuthorDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для детальной информации об авторе,
    включая список его произведений.
    """
    books = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'books']

    def get_books(self, obj):
        # Возвращаем список книг (например, id и title) автора
        return [{'id': book.id, 'title': book.title} for book in obj.books.all()]


class BookSerializer(serializers.ModelSerializer):
    """
    Сериализатор для книги.
    Поле author используется для чтения (вложенное представление автора),
    а author_id – для записи (при создании/обновлении книги).
    """
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True
    )

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',      # вложенное представление автора (read-only)
            'author_id',   # для передачи id автора (write-only)
            'year_of_publication',
            'genre',
            'category',
            'publisher',
            'cover_image',
            'text_file'
        ]