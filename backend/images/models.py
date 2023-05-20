import os
from django.db import models
from orders.models import Order


class OrderImage(models.Model):
    objects = models.Manager()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    original_name = models.CharField(max_length=255)
    project_image_path = models.ImageField(upload_to="order_image/")

    def delete(self, *args, **kwargs):
        # Видаляємо зображення зі зберігального пристрою
        breakpoint()
        os.remove(self.project_image_path.name)
        # Видаляємо запис з бази даних
        super().delete(*args, **kwargs)

# Create your models here.
