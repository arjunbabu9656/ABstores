from django.shortcuts import render, redirect
from cart.models import CartItem, Cart
from cart.views import _cart_id
from .models import Order, Address, OrderItem
import datetime

def checkout(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
            
        for cart_item in cart_items:
            total += (cart_item.product.get_discounted_price() * cart_item.quantity)
            quantity += cart_item.quantity
            
        tax = (2 * total) / 100
        grand_total = float(total) + float(tax)
    except Exception as e:
        pass

    if quantity <= 0:
        return redirect('store')

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': round(grand_total, 2),
    }
    return render(request, 'orders/checkout.html', context)

def place_order(request, total=0, quantity=0):
    current_user = request.user if request.user.is_authenticated else None
    
    # Needs to be logged in to checkout (enforce this here)
    if not current_user:
        return redirect('login')
        
    cart_items = CartItem.objects.filter(user=current_user) if current_user else CartItem.objects.filter(cart__cart_id=_cart_id(request))
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')
        
    for cart_item in cart_items:
        total += (cart_item.product.get_discounted_price() * cart_item.quantity)
        quantity += cart_item.quantity
    tax = (2 * total) / 100
    grand_total = float(total) + float(tax)

    if request.method == 'POST':
        # Retrieve form data
        address = Address.objects.create(
            user=current_user,
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            address_line_1=request.POST['address_line_1'],
            address_line_2=request.POST['address_line_2'],
            city=request.POST['city'],
            state=request.POST['state'],
            country=request.POST['country'],
            pincode=request.POST['pincode'],
        )
        
        # Save order
        order = Order.objects.create(
            user=current_user,
            address=address,
            order_total=grand_total,
            tax=tax,
            is_ordered=True,
            status='Confirmed',
            order_number=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        )
        
        # Move CartItems to OrderItems
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                product_price=item.product.get_discounted_price(),
                ordered=True
            )
            # Reduce product stock
            product = item.product
            product.stock -= item.quantity
            product.save()

        # Clear cart
        cart_items.delete()

        # Redirect to success
        return redirect('order_complete')
    else:
        return redirect('checkout')

def order_complete(request):
    return render(request, 'orders/order_complete.html')
