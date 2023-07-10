from django.db import models
from .validators import validate_timestamp

# Create your models here.


def image_upload_company(instance, filename):
    return f"images/{instance.image.name.upper().replace(' ','@')}/{filename}"


def image_upload_image(instance, filename):
    return f"images/{instance.image.name.lower().replace(' ','-')}/{filename}"


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True, validators=[validate_timestamp])
    created_at = models.DateTimeField(auto_now_add=True)
    uptated_at = models.DateTimeField(auto_now=True)
    tax_price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to=image_upload_image, blank=True, null=True)
    company_logo = models.ImageField(
        upload_to=image_upload_company, blank=True, null=True
    )

    def __str__(self):
        return self.name


class Author(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to=image_upload_image, blank=True, null=True)
    company_logo = models.ImageField(
        upload_to=image_upload_company, blank=True, null=True
    )

    def __str__(self):
        return self.author


class Home(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Fields(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


# REST API
class Test(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    uptadet_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
