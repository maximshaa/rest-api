from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    """
    Модель для хранения информации об авторе.
    Предполагается, что имя автора уникально в базе данных.
    """
    name = models.CharField(max_length=100, unique=True, help_text="Полное имя автора")
    biography = models.TextField(blank=True, null=True, help_text="Биография автора")

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Модель для хранения информации о книге.
    Включает обязательные поля:
    - title: название книги (до 100 символов)
    - author: внешний ключ на модель Author
    - year_of_publication: год выпуска книги (от 1000 до 9999)
    - genre: жанр книги (до 100 символов)
    - category: категория книги (например, 'Художественное произведение', 'Учебник')
    - publisher: издательство (до 100 символов)
    - cover_image: изображение обложки книги
    - text_file: файл с текстом книги

    Уникальность записи обеспечивается комбинацией:
    (название, автор, год выпуска, издательство)
    """
    title = models.CharField(max_length=100, help_text="Название книги")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', help_text="Автор книги")
    year_of_publication = models.IntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(9999)],
        help_text="Год выпуска книги (от 1000 до 9999)"
    )
    genre = models.CharField(max_length=100, help_text="Жанр книги")
    category = models.CharField(max_length=100, help_text="Категория книги (например, 'Художественное произведение' или 'Учебник')")
    publisher = models.CharField(max_length=100, help_text="Издательство книги")
    cover_image = models.ImageField(upload_to='covers/', help_text="Обложка книги")
    text_file = models.FileField(upload_to='books/', help_text="Файл с текстом книги")

    class Meta:
        unique_together = ('title', 'author', 'year_of_publication', 'publisher')
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return f"{self.title} - {self.author.name} ({self.year_of_publication})"
