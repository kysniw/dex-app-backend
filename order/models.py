import os
import uuid

from django.db import models
from django.conf import settings
from user.models import User
from window_sill.models import WindowSill

STATUS_OPTIONS = (
    ('waiting', 'oczekuje'),
    ('accepted', 'zaakceptowane'),
    ('rejected', 'odrzucone'),
    ('paid', 'opłacone'),
    ('awaits_payment', 'oczekuje płatności'),
    ('in_progress', 'w trakcie realizacji')
)

def technical_image_file_path(instance, filename):

    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'technical_draw', filename)

class Order(models.Model):
    order_date = models.DateField(auto_now_add=True)
    order_status = models.CharField(choices=STATUS_OPTIONS, default='waiting')
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    postal_code = models.CharField(max_length=6, default='00-000')
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=150)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email} {self.total_price} {self.order_date}'

class OrderDetail(models.Model):
    sill_width = models.PositiveSmallIntegerField(default=0)
    sill_thickness = models.PositiveSmallIntegerField(default=0)
    sill_length = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=500)
    technical_draw = models.ImageField(null=True, blank=True, upload_to=technical_image_file_path)

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    window_sill = models.ForeignKey(WindowSill, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.window_sill.color_name} {self.sill_width} {self.sill_length}'


