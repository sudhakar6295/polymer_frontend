from django.shortcuts import render
from pl.dataextraction.dataextraction import fetch_categories,fetch_products,fetch_product_detail

# Create your views here.
def index(request):
    categorys = fetch_categories()
    return render(request, 'index.html',{'categorys':categorys})

def search(request):
    #TODO: Implement search functionality
    categorys = fetch_categories()
    return render(request, 'index.html',{'categorys':categorys})

def category(request, category):
    products = fetch_products(category)
    return render(request, 'category.html',{'products':products})

   

def products(request, sku):
    product,images = fetch_product_detail(sku)
    if product:
        return render(request, 'products.html',{'product':product,'images':images})
    else:
        categorys = fetch_categories()
        return render(request, 'index.html',{'categorys':categorys})
    