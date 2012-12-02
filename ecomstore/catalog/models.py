from django.db import models
import datetime

class ActiveCategoryManager(models.Manager):
    """ Manager class to return only those categories where each instance is active """
    def get_query_set(self):
        return super(ActiveCategoryManager, self).get_query_set().filter(is_active=True)
# Create your models here.
class Category(models.Model):
    """ model class containing information about a category in the product catalog """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for product page URL, created automatically from name.')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField(max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for keywords meta tag')
    meta_description = models.CharField(max_length=255,
                                        help_text='Content for description meta tag')
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(default=datetime.datetime.now)
    
    objects = models.Manager()
    active = ActiveCategoryManager()

    class Meta:
        db_table = 'categories'
        ordering = ['name']
        verbose_name_plural = 'Categories'
        
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category', (), { 'category_slug': self.slug })

class ActiveProductManager(models.Manager):
    """ Manager class to return only those products where each instance is active """
    def get_query_set(self):
        return super(ActiveProductManager, self).get_query_set().filter(is_active=True)
    
class Product(models.Model):
    """ model class containing information about a product; instances of this class are what the user
    adds to their shopping cart and can subsequently purchase
    
    """
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Unique value for product page URL, created automatically from name.')
    brand = models.CharField(max_length=50) 
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    old_price = models.DecimalField(max_digits=9,decimal_places=2,
                                    blank=True,default=0.00)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField()
    meta_keywords = models.CharField("Meta Keywords",max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for keywords meta tag')
    meta_description = models.CharField("Meta Description", max_length=255,
                                        help_text='Content for description meta tag')
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(default=datetime.datetime.now)
    categories = models.ManyToManyField(Category)

    image = models.ImageField(upload_to='images/products/main')
    image2 = models.ImageField(upload_to='images/products/main',blank=True)
    image3 = models.ImageField(upload_to='images/products/main',blank=True)
    image4 = models.ImageField(upload_to='images/products/main',blank=True)
   
    thumbnail = models.ImageField(upload_to='images/products/thumbnails')
    thumbnail2 = models.ImageField(upload_to='images/products/thumbnails',blank=True)
    thumbnail3 = models.ImageField(upload_to='images/products/thumbnails',blank=True)
    thumbnail4 = models.ImageField(upload_to='images/products/thumbnails',blank=True)

    image_caption = models.CharField(max_length=200)
    
    objects = models.Manager()
    active = ActiveProductManager()
    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('catalog_product', (), { 'product_slug': self.slug })
    
    @property
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None
    