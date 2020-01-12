from django.db import models
from datetime import datetime


# Create your models here.
class CartItem(models.Model):
    menu = models.CharField(max_length=16)
    size = models.CharField(max_length=16)
    style = models.CharField(max_length=64)
    additional = models.CharField(max_length=255)
    is_special = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, default=0.00, decimal_places=2)
    user_id = models.IntegerField()

    def __str__(self):
        return self.menu + " Price: $" + str(self.price)


class OrderItem(models.Model):
    CHOICES = (
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
    )
    menu = models.CharField(max_length=16)
    size = models.CharField(max_length=16)
    style = models.CharField(max_length=64)
    additional = models.CharField(max_length=255)
    is_special = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, default=0.00, decimal_places=2)
    user_id = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    is_complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']
