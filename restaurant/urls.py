from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:id>', views.menu_item, name='menu_item'),
    # path('menu/<int:id>/new_comment', views.create_comment, name='new_comment')
]