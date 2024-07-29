from django.db import models
from django.urls import NoReverseMatch, reverse


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def str(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True)
    named_url = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    order = models.IntegerField(default=0)

    def str(self):
        return self.title

    def get_absolute_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return "#"
        return self.url or "#"

    class Meta:
        ordering = ["order"]
