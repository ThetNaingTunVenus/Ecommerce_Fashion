from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Category(models.Model):
    status=(('True','True'),('False','False'))
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True,blank=True, related_name='children')
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='category/')
    status = models.CharField(max_length=50, choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    status = (('True','True'),('False', 'False'))
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    image = models.ImageField(null=True, upload_to='product/')
    new_price = models.IntegerField(default=0)
    old_price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    min_amount = models.IntegerField(default=3)
    detail = models.TextField()
    status = models.CharField(max_length=50, choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))
    image_tag.short_description = 'Image'

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def get_absolute_url(self):
        return reversed('category_element', kwargs={'slug':self.slug})


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='product/')

    def __str__(self):
        return self.title

class Setting(models.Model):
    status = (('True','True'),('False','False'))
    title = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    fax = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    smptserver = models.CharField(max_length=200,blank=True)
    smptemail = models.EmailField(max_length=50, blank=True, null=True)
    smptpassword = models.CharField(max_length=200, blank=True)
    smptport = models.CharField(max_length=50, blank=True, null=True)
    icon = models.ImageField(blank=True, null=True, upload_to='icon/')
    facebook = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)
    address = models.TextField()
    contact = models.TextField()
    reference = models.TextField()
    status = models.CharField(max_length=200, choices=status)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
