from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Product, Category

def home(request):
    """Главная страница"""
    return render(request, 'store/home.html')

def product_list(request):
    """Страница со списком всех товаров"""
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_slug):
    """Страница детальной информации о товаре"""
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'store/product_detail.html', {'product': product})


def add_to_cart(request, product_id):
    """Добавление товара в корзину"""
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart

    return redirect('product_list')


def cart_view(request):
    """Просмотр корзины"""
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        item_total = product.price * quantity
        total_price += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': item_total
        })

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def update_cart(request, product_id):
    """Обновление количества товара в корзине"""
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if quantity > 0:
            cart[str(product_id)] = quantity
        else:
            # Если количество 0 или меньше - удаляем товар
            cart.pop(str(product_id), None)

        request.session['cart'] = cart

    return redirect('cart_view')


def remove_from_cart(request, product_id):
    """Удаление товара из корзины"""
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart_view')

def clear_cart(request):
    """Очистка всей корзины"""
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('cart_view')

