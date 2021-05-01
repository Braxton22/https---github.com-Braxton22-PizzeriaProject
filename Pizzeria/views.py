from django.shortcuts import render, redirect
from .models import Pizza
from .forms import CommentForm

# Create your views here.

def index(request):
    '''the home page for the Pizzeria'''
    return render(request, 'Pizzeria/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('name')
    
    context = {'pizzas':pizzas}

    return render(request, 'Pizzeria/pizzas.html', context)

def pizza(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    comments = pizza.comment_set.order_by('-date_added')
    context = {'pizza':pizza,'toppings':toppings, 'comments':comments}

    return render(request,'Pizzeria/pizza.html',context)

#GET requests for pages only read data from the server
#POST requests writes data through a form to the server
def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            form.save()
            return redirect('Pizzeria:pizza', pizza_id= pizza_id)
    
    context = {'form':form,'pizza': pizza}
    return render(request,'Pizzeria/new_comment.html', context)
