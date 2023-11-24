from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http.response import HttpResponse
from .models import UserComments, MenuItem, Rating, Cart, CartItem
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import CommentForm, RatingForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def menu(request):
    items = MenuItem.objects.all()
    context = {'items': items}
    return render(request, 'menu.html', context)

# Menu Items viewsets integrated with comment section, but it lacked the option to 
# Authenticate before creating a comment data set.

# @login_required()
# def menu_item(request, id):
#     item = MenuItem.objects.get(pk=id)
#     comments = item.comments.all()
#     current_user = request.user
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment_text = form.cleaned_data['comment']
#             item.comments.create(user=request.user, comment=comment_text)
            
#             return redirect('menu_item', id=item.id)
#     else:
#         form = CommentForm()
    
#     context = {'item':item, 'comments':comments, 'form':form}
#     return render(request, 'menu_item.html', context)

def create_comment(request, id):
    item = MenuItem.objects.get(pk=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data['comment']
            item.comments.create(user=request.user, comment=comment_text)
            
            return redirect('menu_item', id=item.id)



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        
    else:
        form = UserCreationForm()
            
        return render(request, 'registration/signup.html', {'form':form})
    
    
def login(request):
    if request.method == 'POST':
        pass
    
    
    
    
def menu_item(request, id):
    item = MenuItem.objects.get(pk=id)
    ratings = Rating.objects.filter(menu_item=item)
    rating_form = RatingForm()
    comments = item.comments.all()
    form = CommentForm()
    context = {'item':item, 'comments':comments, 'form':form, 'rating_form': rating_form}
    return render(request, 'menu_item.html', context)


def submit_rating(request, id):
    menu_item = MenuItem.objects.get(pk=id)
    
    if request.method == 'POST':
        # form = RatingForm(request.POST)
        # if form.is_valid():
        #     rating = form.save(commit=False)
        #     rating.user = request.user
        #     rating.menu_item = menu_item.id
        #     rating.save()
            
        #     # Update average rating for that specific menu item
        #     menu_item.update_rating()
            
        #     return redirect('menu_item.html', id=menu_item.id)
        
        
        form = RatingForm(request.POST)
        form.instance.user = request.user
        form.instance.menu_item = menu_item
        
        if form.is_valid():
            form.save()
            menu_item.update_rating()
            
            return redirect('menu_item', id=menu_item.id)
        else:
            messages.error(request, "Failed to submit form, Please check the form.")
    else:
        form = RatingForm()
        
    return render(request, 'menu_item.html', {'menu_item':menu_item, 'rating_form':form})
        
        
def about(request):
    return render(request, 'about.html', {})



def add_to_cart(request, cartitem_id):
    if request.user.is_authenticated:
        menu_item = get_object_or_404(MenuItem, pk=cartitem_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        
        if cart.user is None:
            cart.user = request.user
            cart.save()
            
            
        cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart,user=request.user, item=menu_item, defaults={'quantity': 1})
        
        if not cart_item_created:
            cart_item.quantity +=1
            cart_item.save()
            
    
    return redirect('menu')


def view_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.cartitem_set.all()
        total_price = sum(item.item.price * item.quantity for item in cart_items)
        
        return render(request, 'view_cart.html', {'cart_items':cart_items, 'total_price': total_price})
    
    # Redirect to login page if user is not authenticated
    return redirect('login')

def cart_items(request):
    user_cart_items = []
    
    if request.user.is_authenticated:
        user_cart_items = CartItem.objects.filter(cart__user=request.user)
        
        
    return render(request, 'cart.html', {'user_cart_items':user_cart_items})