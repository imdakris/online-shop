from django.core.paginator import Paginator
from django.shortcuts import render

from goods.models import Products


# Create your views here.
def catalog(request, category_slug):
    '''Slug converter for categories'''
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(1)

    context = {
        "title": "Home - Каталог",
        "goods": current_page,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)
