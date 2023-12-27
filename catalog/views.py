from django.shortcuts import render
from catalog.models import Category, Brand, Product, Offer


def index(request):
    brands = Brand.objects.all().order_by('name')
    categories = Category.objects.filter(parent=None).filter(brand=None)
    brand_categories = Category.objects.filter(parent=None).exclude(brand=None)
    context = {'brands': brands, 'categories': categories, 'brand_categories': brand_categories}
    return render(request, 'index.html', context=context)


def get_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    try:
        brand = Brand.objects.get(id=category.brand_id)
    except Brand.DoesNotExist:
        brand = None
    # todo: decide which option is better
    parent = category.parent
    if parent is not None:
        parent = Category.objects.get_(pk=parent.id)
    children = Category.objects.filter(parent=category.id)
    products = Product.objects.filter(categories=category.id)
    context = {'category': category,
               'parent': parent,
               'brand': brand, 'children': children, 'products': products}
    return render(request, 'catalog/category.html', context=context)


def get_product_with_offers(request, brand_id, product_id):
    offers = Offer.objects.filter(product=product_id)
    product = Product.objects.get(id=product_id)
    brand = Brand.objects.get(pk=brand_id)
    context = {'offers': offers, 'product': product, 'brand_id': brand}
    return render(request, 'catalog/product_with_offers.html', context=context)
