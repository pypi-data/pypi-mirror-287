# Tree Menu

A Django app for creating tree menus.

## Installation

Install the app using pip:

```sh
pip install tree_menu322
```
Add tree_menu to your INSTALLED_APPS:

```python

INSTALLED_APPS = [
    ...
    'tree_menu',
]
```

Use the draw_menu template tag in your templates:

```html

{% load menu_tags %}
{% draw_menu 'main_menu' %}
```