from django.shortcuts import render, redirect
from items.models import Item, Cart

# Create your views here.
def item_index(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items/item_index.html", context)

def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        "item": item
    }
    return render(request, "items/item_detail.html", context)

def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.item.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, pk):
    item = Item.objects.get(id=pk)
    cart_item, created = Cart.objects.get_or_create(item=item, 
                                                    user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

def remove_from_cart(request, pk):
    cart_item = Cart.objects.get(id=pk)
    cart_item.delete()
    return redirect("view_cart")