from django.db import models

# Create your models here.


class Pizza(models.Model):
    """Pizza model"""

    name = models.TextField(max_length=79)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)


class Topping(models.Model):
    name = models.TextField(max_length=69)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)
