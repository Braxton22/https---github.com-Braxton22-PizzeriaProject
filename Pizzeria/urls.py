#need the path function to map a url to a view
from django.urls import path

#dot tells python to import views.py module from the same directory as the current urls.py module
from . import views

#the variable app_name helps Django distinguish this urls.py file from the files of the same name in other apps within the project
app_name = 'Pizzeria'

#the variable urlpatterns in this moudle is a list of individual pages that can be requested form the Pizzeria app 
urlpatterns = [
    #the empty string matches the base url (nothing in there), the second argument calls in views, and t he third provides index for this url pattern to refer to it later
    path('',views.index,name='index'),
    path('pizzas',views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/',views.pizza,name='pizza'),
    path('new_comment/<int:pizza_id>/',views.new_comment,name='new_comment')
]