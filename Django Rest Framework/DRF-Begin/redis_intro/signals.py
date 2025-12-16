from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.core.cache import cache
from .models import Products


@receiver([post_save, post_delete], sender=Products)
def invalidate_products_list_cache(sender, instance, *args, **kwargs):
    # cache.clear()

    # invalidate all the keys that has keyprefix= product_list
    cache.delete_pattern("*product_list*")
