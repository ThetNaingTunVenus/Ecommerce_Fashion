from django.db import models

# Create your models here.
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
