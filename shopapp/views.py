from timeit import default_timer

from django.http import HttpResponse
from django.shortcuts import render

def shop_index(request):
    context = {
        "time_running": default_timer(),
    }
    return render(request, "shopapp/shop-index.html", context=context)
