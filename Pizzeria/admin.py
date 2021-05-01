from django.contrib import admin

# Register your models here.
from .models import Pizza, Topping, Comment #the dot tells Django to look for models.py in teh same directory

admin.site.register(Pizza) #the code admin.site.register() tells Django to manage our model through the admin site
admin.site.register(Topping)
admin.site.register(Comment)