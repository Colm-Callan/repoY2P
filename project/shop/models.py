from django.db import models
import uuid
from django.urls import reverse

class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'category', blank=True)
    
    ROOM_CHOICES = [
        ('bedroom', 'Bedroom'),
        ('kitchen', 'Kitchen'),
        ('living_room', 'Living Room'),
        ('bathroom', 'Bathroom'),
        ('garden', 'Garden'),
    ]
    
    room = models.CharField(max_length=200, choices=ROOM_CHOICES, default=None)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:products_by_category', args=[self.id])
    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to = 'product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    loyal_product = models.BooleanField(default=False)
    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.category.id, self.id]
)
    def __str__(self):
        return self.name