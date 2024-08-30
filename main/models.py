from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=155,  null=True, blank=True)
    class Meta(AbstractUser.Meta):
        swappable  = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Banner(models.Model):
    price = models.IntegerField()
    title = models.CharField(max_length=255)
    addition = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Banner_image/')


class Support(models.Model):
    title = models.CharField(max_length=155)
    more = models.CharField(max_length=155)
    title2 = models.CharField(max_length=155)
    more2 = models.CharField(max_length=155)
    title3 = models.CharField(max_length=155)
    more3 = models.CharField(max_length=155)

class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_image/')
    is_sale = models.FloatField(default=0)
    old_price = models.DecimalField(max_digits=10 , decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    shipping_police = models.TextField()
    rating = models.FloatField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    vendors = models.ForeignKey(to='Vendors', on_delete=models.CASCADE)
    size = models.ForeignKey(to='Size', on_delete=models.CASCADE)
    color = models.ForeignKey(to='Color', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Vendors(models.Model):
    name = models.CharField(max_length=255)


class Size(models.Model):
    name = models.CharField(max_length=255)


class Color(models.Model):
    name = models.CharField(max_length=255)


class Image(models.Model):
    name = models.ImageField(upload_to='Image/')


class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Blog_image/')
    admin = models.CharField(max_length=255)
    data = models.DateField(auto_now=True)
    description = models.TextField()
    article = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='About_image/')


class Team(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='Team_photo/')


class Information(models.Model):
    title = models.CharField(max_length=155)
    info = models.CharField(max_length=155)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'

        ), ])
    message = models.TextField()


class Comment(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    blog = models.ForeignKey(to='Blog', on_delete=models.PROTECT)
    text = models.TextField()
    date = models.DateField(auto_now=True)


class Cart(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    product = models.ForeignKey(to='Product', on_delete=models.PROTECT)


