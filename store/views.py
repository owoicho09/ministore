from django.shortcuts import render
from .models import Products, ItemGallery, Items
from django.http import JsonResponse

# Create your views here.


def index(request):
    products = Products.objects.all()
    product = Products.objects.filter(product_id='mpbrOhMHzR').first()

    # If the product is found, retrieve all associated items
    if product:
        items = Items.objects.filter(product=product, featured=True)
    for p in products:
        print('--',p.name)
    print(products)
    context = {
        'products':products,
        'items':items

    }

    return render(request, 'store/index.html', context)

def item_page(request, product_id):
    product = Products.objects.get(product_id=product_id)
    items = Items.objects.filter(product=product, sold=False, featured=True)

    context = {
        'items':items

    }
    return render(request, 'store/item_page.html', context)


def search(request):
    query = request.GET.get('q', '')  # Get query with fallback to empty string
    items = []

    if query:  # Only search if there's input
        items = Items.objects.filter(name__icontains=query)  # Descending order

    context = {
        'query': query,
        'items': items
    }

    return render(request,'store/search.html',context)



def live_search(request):
    query = request.GET.get('q', '')  # Get the query parameter
    results = []

    if query:  # Check if query is not empty
        items = Items.objects.filter(name__icontains=query)
        results = list(items.values('id','name', 'price'))  # Convert to JSON-friendly format

    return JsonResponse({'results': results})