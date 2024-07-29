from django.urls import path
from .views import test_view, menu_item

app_name = "tree_menu"

urlpatterns = [
    path("test/", view=test_view, name="test_view"),
    path("menu/<int:id>/", view=menu_item, name="menu_item"),
]