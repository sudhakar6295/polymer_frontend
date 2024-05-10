from pl.models import Products, Images

def fetch_categories():
    unique_categories = Products.objects.values_list('categories', flat=True).distinct()
    return unique_categories


def fetch_products(category):
    products = Products.objects.filter(categories=category).values('product_title', 'sku','main_image_url','normal_price')
    return products

def fetch_product_detail(sku):
    product = Products.objects.filter(sku=sku).values().first()
    images = Images.objects.filter(sku=sku).values('image_url')
    if product is None:
        return None,None
    return product,images