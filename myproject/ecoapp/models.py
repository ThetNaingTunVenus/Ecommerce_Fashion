from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
from django.utils.safestring import mark_safe


class Category(MPTTModel):
    status=(('True','True'),('False','False'))
    parent = TreeForeignKey('self',on_delete=models.CASCADE, null=True,blank=True, related_name='children')
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='category/')
    status = models.CharField(max_length=50, choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

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

class HeadBanner(models.Model):
    status = (('True', 'True'), ('False', 'False'))
    title = models.CharField(max_length=200)
    sale_offer = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='banner/', blank=True, null=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    status = (('New','New'),('Read','Read'),('Closed','Closed'))
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=50, choices=status, default='New')
    ip = models.CharField(max_length=200, blank=True)
    note = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ShopCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()



    def price(self):
        return self.product.new_price
    @property
    def amount(self):
        return self.quantity*self.product.new_price


    def __str__(self):
        return self.product.title


class Order(models.Model):
    status = (('New', 'New'), ('Accepted', 'Accepted'), ('Prepared', 'Prepared'),('Completed','Completed'),('Cancelled','Cancelled'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, editable=False)
    phone = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200, blank=True)
    total = models.IntegerField()
    status = models.CharField(max_length=50, choices=status, default='New')
    ip = models.CharField(max_length=200, blank=True)
    transaction_id = models.CharField(max_length=200, blank=True)
    transaction_image = models.ImageField(upload_to='transaction_img/', blank=True)
    adminnote = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))
    image_tag.short_description = 'Image'


class OrderProduct(models.Model):
    status = (('New', 'New'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'))
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    amount = models.IntegerField()
    status = models.CharField(max_length=50, choices=status, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title

    def amount_now(self):
        return self.price*self.quantity


class Comment(models.Model):
    status = (('New','New'),('True','True'),('False','False'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, blank=True)
    comment = models.CharField(max_length=200, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=50, choices=status, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
