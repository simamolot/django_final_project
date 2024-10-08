from django.db import models

class Apartment(models.Model):
    title = models.CharField(max_length=120, verbose_name='Title of the house')
    description = models.TextField(verbose_name='Room description')
    city = models.CharField(max_length=150, null=False, default=None, verbose_name='City')
    street = models.CharField(max_length=120, verbose_name='Address')
    house_number = models.CharField(max_length=120, verbose_name='House number')
    amount_of_rooms = models.IntegerField(verbose_name='Count of rooms')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    is_active = models.BooleanField(default=True)
    type_of_housing = models.CharField(max_length=200, verbose_name='Describe your housing type')

    def __str__(self):
        return self.title, self.description