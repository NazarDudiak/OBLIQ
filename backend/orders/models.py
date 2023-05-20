from django.db import models


class Order(models.Model):
    objects = models.Manager()

    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    address = models.CharField("Address", max_length=255)
    phone = models.CharField(max_length=20)
    registrationDate = models.DateField("Order Date", auto_now_add=True)

    def __str__(self):
        return self.name
