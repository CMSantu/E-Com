from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SearchForm,CheckoutForm,CartForm

def home(request):
    form = SearchForm(request.GET or None)
    products = Product.objects.all()

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            products = products.filter(name__icontains=query)

    return render(request, 'shop/home.html', {'products': products, 'form': form})

def about_us(request):
    return render(request,'shop/aboutus.html')

def category_list(request):
    categories = Category.objects.all() 
    return render(request, 'shop/categories.html', {'categories': categories})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/category_products.html', {'category': category, 'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'shop/signup.html', {'form': form})

@login_required
def remove_from_cart(request, pk):
    cart_item = OrderItem.objects.get(id=pk)
    cart_item.delete()
    cart = Order.objects.get(user=request.user)
    #cart.total_price -= cart_item.product.price * cart_item.quantity
    cart.save()
    return redirect('cart')

@login_required
def update_cart(request, pk):
    cart_item = OrderItem.objects.get(id=pk)
    form = CartForm(request.POST or None, instance=cart_item)
    if form.is_valid():
        form.save()
        cart = Order.objects.get(user=request.user)
        #cart.total_price = sum([item.product.price * item.quantity for item in Order.objects.filter(cart=cart)])
        cart.save()
        return redirect('cart')
    return render(request, 'shop/update_cart.html', {'form': form, 'cart_item':cart_item})


@login_required
def checkout(request):
    cart_items = OrderItem.objects.filter()
    
    if not cart_items:
        return redirect('cart') 
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            return redirect('success')
    else:
        form = CheckoutForm()

    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'shop/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'form': form
    })



@login_required
def cart(request):
    user_order, created = Order.objects.get_or_create(user=request.user, status='Pending')
    items = user_order.items.all()
    total_price = sum(item.product.price * item.quantity for item in items)
    return render(request, 'shop/cart.html', {'items': items,'total_price': total_price})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user_order, created = Order.objects.get_or_create(user=request.user, status='Pending')
    order_item, created = OrderItem.objects.get_or_create(order=user_order, product=product, defaults={'price': product.price, 'quantity': 1})
    if not created:
        order_item.quantity += 1
        order_item.save()
    user_order.save()
    return redirect('cart')

def logout(request):
    auth_logout(request)
    return redirect('home')


def success(request):
    # user_order, created = Order.objects.get_or_create(user=request.user, status='Success')
    return render(request, 'shop/success.html')

def clear_cart(request):
    user_order, created = Order.objects.get_or_create(user=request.user)
    cart_items = OrderItem.objects.filter()
    order_cart=Order.objects.all()
    cart_items.delete()
    order_cart.delete()
    user_order.total_price=0
    user_order.save()
    return redirect('home')



    # admin user ID- cms
    # admin pwd- 14325268