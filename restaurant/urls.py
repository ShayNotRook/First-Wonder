from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('home/', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:id>', views.menu_item, name='menu_item'),
    # path('menu/<int:id>/new_comment', views.create_comment, name='new_comment'),
    path('home/login/', auth_views.LoginView.as_view(template_name='registration/login.html', success_url=reverse_lazy('home')) ,name='login'),
    path('home/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/signup/', views.signup, name='signup'),
]