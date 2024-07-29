from django import template
from django.urls import resolve, reverse, NoReverseMatch
from ..models import Menu, MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context["request"]
    current_url = request.path

    try:
        menu = Menu.objects.prefetch_related("items__children").get(name=menu_name)
    except Menu.DoesNotExist:
        return ""

    def build_menu(items, parent=None):
        result = []
        for item in items:
            if item.parent == parent:
                children = build_menu(items, item)
                url = item.get_absolute_url()
                is_active = (url == current_url or
                             any(child["is_active"] for child in children) or
                             resolve(current_url).url_name == item.named_url)
                result.append(
                    {
                        "title": item.title,
                        "url": url,
                        "children": children,
                        "is_active": is_active,
                    }
                )
        return result

    menu_items = build_menu(menu.items.all())

    return template.loader.render_to_string(
        "tree_menu/menu.html",
        {
            "menu_items": menu_items,
        },
    )