from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from userauth.models import User
import string
from cloudinary import uploader
import cloudinary
from cloudinary.models import CloudinaryField
from django.conf import settings

# Create your models here.

cloudinary.config(
    cloud_name=settings.CLOUD_NAME,
    api_key=settings.API_KEY,
    api_secret=settings.API_SECRET
)


class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True, db_index=True)
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=20, null=True, blank=True)
    product_id = ShortUUIDField(unique=True, length=10, max_length=20, alphabet=string.ascii_letters + string.digits)

    def __str__(self):
        return self.name


class Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True, blank=True)
    name = models.CharField(max_length=300, db_index=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    description = models.TextField(null=True, blank=True)  # Add optional description

    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, null=True, blank=True)
    sold = models.BooleanField(default=False)
    featured = models.BooleanField(default=True)
    item_id = ShortUUIDField(unique=True, length=10, max_length=20, alphabet=string.ascii_letters + string.digits)

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == '':
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def thumbnail(self):
        if self.image:
            return mark_safe(
                f"<img src='{self.image.url}' width='50' height='50' style='object-fit: cover; border-radius: 6px;' />")
        return "No Image"

    def item_gallery(self):
        return ItemGallery.objects.filter(item=self)


class ItemGallery(models.Model):
    item = models.ForeignKey(Items,on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True, blank=True)
    igid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet=string.ascii_letters + string.digits)

    def __str__(self):
        return self.hostel.name

    def thumbnail(self):
        if self.image:
            return mark_safe(
                f"<img src='{self.image.url}' width='50' height='50' style='object-fit: cover; border-radius: 6px;' />")
        return "No Image"