from django.db.models.signals import post_save, post_delete
# import reciever to get signals
from django.dispatch import receiver
from .models import OrderLineItem


# execute this anytime the post_save signal is sent
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    print('delete signal received!')
    instance.order.update_total()
