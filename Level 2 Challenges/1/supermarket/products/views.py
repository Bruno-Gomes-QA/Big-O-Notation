from django.shortcuts import render
from .models import Product
from .forms import ProductSearchForm

def product_search(request):
    form = ProductSearchForm(request.GET)
    products = []

    if form.is_valid():
        query = form.cleaned_data['query']
        products = Product.objects.filter(name__icontains=query)

    return render(request, 'products/product_search.html', {'form': form, 'products': products})
