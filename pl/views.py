from django.shortcuts import render
from pl.dataextraction.dataextraction import fetch_categories,fetch_products,fetch_product_detail,search_product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from json import dumps 

# Create your views here.
def index(request):
    categorys = fetch_categories()
    return render(request, 'index.html',{'categorys':categorys})

def search(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query']
        product, images = search_product(query)
        if product :
            stock = renderstock(product.get('stock'))
            return render(request, 'products.html', {'product': product, 'images': images,'stock':stock})
    
    categorys = fetch_categories()
    return render(request, 'index.html', {'categorys': categorys})

def renderstock(stockDictionary={}):
 
    # dump data 
    dataJSON = dumps(stockDictionary) 
    return dataJSON

def category(request, category):
    products = fetch_products(category)
    total_products = len(products)
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 12)
    try:
        items = paginator.page(page)

    except PageNotAnInteger:
        items = paginator.page(1)

    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    start_index = items.start_index()
    end_index = items.end_index()

    return render(request, 'category.html',{'products':items,'page':items,'start_index':start_index,'end_index':end_index,'total_products':total_products})

   

def products(request, sku):
    product,images = fetch_product_detail(sku)

    if product:
        stock = renderstock(product.get('stock'))
        return render(request, 'products.html',{'product':product,'images':images,'stock':stock})
    else:
        categorys = fetch_categories()
        return render(request, 'index.html',{'categorys':categorys})
    