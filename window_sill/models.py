import os
import uuid

from django.db import models


UNIT_PRICES = (
    ('mb', 'mb'),
    ('m2', 'm2'),
)

MANUFACTURERS = (
    ('dex', 'dex'),
    ('kobax', 'kobax'),
    ('wiech', 'wiech'),
)


def sill_image_file_path(instance, filename):

    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'recipe', filename)


class AdditionalOption(models.Model):
    option_name = models.CharField(max_length=50)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    price_unit = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.option_name


class SillCategory(models.Model):

    category_name = models.CharField(max_length=255)
    price_unit = models.CharField(choices=UNIT_PRICES, default='mb')
    manufacturer = models.CharField(choices=MANUFACTURERS, default='dex')
    max_length = models.PositiveSmallIntegerField(default=6000)
    min_length = models.PositiveSmallIntegerField(default=5)
    max_width = models.PositiveSmallIntegerField(default=1000)
    min_width = models.PositiveSmallIntegerField(default=5)
    additional_options = models.ManyToManyField(AdditionalOption)

    def __str__(self):
        return self.category_name + " - " + self.manufacturer


class SillWidth(models.Model):
    width = models.PositiveSmallIntegerField(default=5)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return str(self.width) + 'mm (szer.) | ' + str(self.price) + ' zł'


class SillThickness(models.Model):
    thickness = models.PositiveSmallIntegerField(default=5)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return str(self.thickness) + 'mm (gr.) | ' + str(self.price) + ' zł'


class WindowSill(models.Model):
    color_name = models.CharField(max_length=255)
    width_option = models.ManyToManyField(SillWidth, blank=True)
    thickness_option = models.ManyToManyField(SillThickness, blank=True)
    sill_category = models.ForeignKey(
        SillCategory, on_delete=models.CASCADE, default=0)
    image = models.ImageField(null=True, upload_to=sill_image_file_path)

    def __str__(self):
        return self.sill_category.category_name + ' | ' + self.color_name
