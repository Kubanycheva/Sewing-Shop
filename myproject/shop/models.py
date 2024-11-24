from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)


class Catalog(models.Model):
    catalog_name = models.CharField(max_length=32)
    description = models.TextField()
    catalog_image = models.ImageField(upload_to='catalog_images')

    def __str__(self):
        return self.catalog_name


class NameProduct(models.Model):
    catalog_name = models.CharField(max_length=32)
    description = models.TextField()
    catalog_image = models.ImageField(upload_to='product_images')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.product_name


class Company(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.title


class CompanyPhotos(models.Model):
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='company_images/')

asdfghjk


