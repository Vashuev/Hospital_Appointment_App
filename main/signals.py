from django.contrib.auth.models import User, Group
from .models import Patient
from django.db.models.signals import post_save


def create_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='patient')
        instance.groups.add(group)
        Patient.objects.create(
            user= instance,
            name = instance.username,
            email = instance.email
        )

post_save.connect(create_profile, sender=User)