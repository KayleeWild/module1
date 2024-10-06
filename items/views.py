from django.shortcuts import render, redirect
from items.models import Item, Cart
from .forms import CheckoutForm

# home page displaying all products
def item_index(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items/item_index.html", context)
# page that shows more info about the product when "read more" button is pushed
def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        "item": item
    }
    return render(request, "items/item_detail.html", context)
# cart page
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.item.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})
# route to get to cart when "add to cart" button is pushed
def add_to_cart(request, pk):
    item = Item.objects.get(id=pk)
    cart_item, created = Cart.objects.get_or_create(item=item, 
                                                    user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')
# stays on cart page, just removes the item from your cart
def remove_from_cart(request, pk):
    cart_item = Cart.objects.get(id=pk)
    cart_item.delete()
    return redirect("view_cart")
# page where checkout occurs
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.item.price * item.quantity for item in cart_items)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # This is where you would do stuff with the form
            return redirect("success")
    else:
        form = CheckoutForm()
    return render(request, 'cart/checkout.html', {'total_price': total_price,'form': form})
# processes the form
def success_view(request):
    return render(request, 'success.html')