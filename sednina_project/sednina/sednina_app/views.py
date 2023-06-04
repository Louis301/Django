from django.shortcuts import render
from . models import Product, Order


def home(request):
    return render(request, 'home.html') 

def about(request):
    return render(request, 'about.html') 


def products(request):
    all_products = Product.objects.all()
    categories = ['Декоративно-лиственные растения', 'Кактусы и суккуленты', 'Растения-крупномеры']

    if request.POST.get('expend_order') == "В корзину":

        from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
        try:
            product = Product.objects.get(title=request.POST.get('product_title'))

            if len(Order.objects.all()) > 0 and len(Order.objects.filter(title=product.title)) > 0:
                print("Товар уже в списке")
            else:
                Order.objects.create(
                    title=product.title,
                    price=product.price,
                    image=product.image,
                    category=product.category,
                )
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            pass

    return render(request, 'products.html', {'all_products':all_products, 'categories':categories})
 

def order(request):
    total_order = 0
    order = Order.objects.all()

    for product in order:
        total_order += product.price

    return render(request, 'order.html', {'order' : order, "total_order":total_order}) 