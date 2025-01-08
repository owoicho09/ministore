from django.shortcuts import render
from .models import Products, ItemGallery, Items
from django.http import JsonResponse

# Create your views here.


def index(request):
    products = Products.objects.all()
    featured_tools = Products.objects.filter(product_id='JlZiLJKEwf').first()
    featured_motorpart = Products.objects.filter(product_id='2uxQmSrbSZ').first()
    featured_shoes = Products.objects.filter(product_id='wTUkfGy7i4').first()
    featured_clothes = Products.objects.filter(product_id='uOinM1l5WQ').first()

    # If the product is found, retrieve all associated items
    items = motorpart = shoes = clothes = []

    # If any featured product is found, retrieve associated items
    if featured_tools:
        items = Items.objects.filter(product=featured_tools, featured=True)
    if featured_motorpart:
        motorpart = Items.objects.filter(product=featured_motorpart, featured=True)
    if featured_shoes:
        shoes = Items.objects.filter(product=featured_shoes, featured=True)
    if featured_clothes:
        clothes = Items.objects.filter(product=featured_clothes, featured=True)

    # Add the context variables to pass them to the template
    context = {
        'products': products,
        'featured_tools_items': items,
        'featured_motorpart_items': motorpart,
        'featured_shoes_items': shoes,
        'featured_clothes_items': clothes
    }

    return render(request, 'store/index.html', context)

def item_page(request, product_id):
    product = Products.objects.get(product_id=product_id)
    items = Items.objects.filter(product=product, sold=False)

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