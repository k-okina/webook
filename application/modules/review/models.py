from django.db import models
from submodules.custom_model_fields import IntegerRangeField
from settings import AUTH_USER_MODEL


class Review(models.Model):
    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=False)
    book = models.ForeignKey(to='book.Book', on_delete=False)
    text = models.TextField()
    star = IntegerRangeField(min_value=1, max_value=5)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_all(cls) -> list:
        return list(cls.objects.all().order_by('-created_at'))

    @classmethod
    def get_by_user_with_book(cls, user, book):
        return cls.objects.get(user=user, book=book)

    @classmethod
    def get_by_book(cls, book) -> list:
        return list(cls.objects.filter(book=book).order_by('-created_at'))

    @classmethod
    def get_by_id(cls, pk: int):
        return cls.objects.get(pk=pk)

    @classmethod
    def is_exists(cls, user, book) -> bool:
        return cls.objects.filter(user=user, book=book).exists()

    def __str__(self):
        return 'star: [{0}], short body: [{1}]'.format(self.star,
                                                       self.text[0:10])
