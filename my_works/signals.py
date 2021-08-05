from django.db.models.signals import pre_delete
from .models import (
    Articles,
    Books,
    Presentations,
    Projects,
    Events, 
    Videos,
)                                                   # signal sender

from django.dispatch import receiver

@receiver(pre_delete, sender=Articles)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete()

@receiver(pre_delete, sender=Books)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete()

@receiver(pre_delete, sender=Presentations)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete()

@receiver(pre_delete, sender=Projects)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete()

@receiver(pre_delete, sender=Events)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete()

@receiver(pre_delete, sender=Videos)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete()