from django.db import models


class Products(models.Model):
    sku = models.CharField(max_length=50, primary_key=True)
    product_url = models.CharField(max_length=255)
    product_title = models.CharField(max_length=255)
    normal_price = models.CharField(max_length=50)
    discount_price = models.CharField(max_length=50)
    stock = models.JSONField()
    categories = models.CharField(max_length=255)
    subcategories = models.CharField(max_length=255)
    breadcrumb = models.CharField(max_length=255)
    weight = models.CharField(max_length=50)
    dimension = models.CharField(max_length=255)
    height = models.CharField(max_length=50)
    width = models.CharField(max_length=50)
    length = models.CharField(max_length=50)
    approximate_weight = models.CharField(max_length=50)
    descriptions = models.TextField()
    short_description = models.TextField()
    LastScrappeddate = models.DateTimeField(auto_now=True)
    Updateddate = models.DateTimeField(auto_now=True)
    Createddate = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=50)
    main_image_url = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'products'
        

class Images(models.Model):
    image_url = models.CharField(max_length=255, primary_key=True)
    sku = models.CharField(max_length=50, db_index=True)  # Assuming this is a foreign key, no need for ForeignKey field in Django
    class Meta:
        db_table = 'images'
