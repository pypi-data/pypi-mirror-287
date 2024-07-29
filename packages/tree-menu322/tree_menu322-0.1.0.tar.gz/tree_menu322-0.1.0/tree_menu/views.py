from django.shortcuts import render, get_object_or_404
from .models import  MenuItem
from django.http import HttpResponse

def test_view(request):
    return render(request, "tree_menu/test.html")

def menu_item(request, id):
    item = get_object_or_404(MenuItem, id=id)
    return HttpResponse(item.title)
