from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('menu/<int:id>', views.menu_item, name='menu_item'),
    path('menu/<int:id>/create_comment', views.create_comment, name='create_comment'),
    # path('menu/<int:id>/new_comment', views.create_comment, name='new_comment'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html') ,name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('menu/<int:id>/submit_rating', views.submit_rating, name='submit_rating'),
]