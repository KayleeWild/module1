from django.shortcuts import render
from items.models import Item

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