from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import UserComments, MenuItem
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def menu(request):
    items = MenuItem.objects.all()
    context = {'items': items}
    return render(request, 'menu.html', context)


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
    comments = item.comments.all()
    form = CommentForm()
    context = {'item':item, 'comments':comments, 'form':form}
    return render(request, 'menu_item.html', context)