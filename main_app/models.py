from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from PIL import Image # pillow image manipulation
from django.dispatch import receiver
from django.db.models.signals import post_save
# from django.forms import ModelForm

RSVP_CHOICES = [
    ('Absolutely!', 'Absolutely!'),
    ('Not quite certain', 'Not quite certain'),
    ('Unfortunately, no...', 'Unfortunately, no...'),
]

# Create your models here.
class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, default='anonymous')
    rsvp = models.CharField(max_length=30, choices=RSVP_CHOICES) 
    # should allow user a 3 options instead of BOOL
    def __str__(self): # django-admin: what Guests show up as. Most things cause errors...?
        return self.name

@ receiver(post_save, sender=User)
def create_guest(sender, instance, created, **kwargs):
    if created:
        Guest.objects.create(user=instance)
# when user object is created, create a Guest instance



class Post(models.Model):
    title = models.CharField(default="", max_length=150)
    body = models.CharField(default="", max_length=999)
    created_at = models.DateTimeField(auto_now_add=True)
    image = ImageField(upload_to='media/', blank=True) # optional (come back to this last, not MVP)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): # django-admin: what Posts show up as 
        return str(self.title)

    class Meta:
        ordering = ['created_at']

