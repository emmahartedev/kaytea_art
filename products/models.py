from django.db import models
from django.core.validators import MaxValueValidator

from django.contrib.auth.models import User  


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    date_added = models.DateTimeField(auto_now_add=True) 
    sku = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    size = models.TextField()
    media = models.TextField()
    stock = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


RATING = (
    (' ', 'Rating *'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class ProductReview(models.Model):
    author = models.ForeignKey(User, null=True,
                               blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, related_name='reviews',
                                on_delete=models.CASCADE)
    review_text = models.TextField()
    review_rating = models.CharField(choices=RATING,
                                     max_length=1,
                                     default=" ",
                                     null=True)

    def __str__(self):
        return f'{self.product} review by {self.author}'
