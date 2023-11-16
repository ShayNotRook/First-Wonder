from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title= models.CharField(max_length=255)
    def __str__(self):
        return self.title
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    # slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.title
    
class UserComments(models.Model):
    
    ratings = (
        ( 1 , 'One Star'),
        ( 2 , 'Two Stars'),
        ( 3, 'Three Stars'),
        ( 4 , 'Four Stars'),
        ( 5 , 'Five Stars') 
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=255)
    rating = models.SmallIntegerField(default=1, choices=ratings)
    comment = models.TextField(max_length=8000)
    created_at = models.DateTimeField(default=timezone.now)
    helpful = models.BooleanField(default=False)
    reply_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, default=1, related_name='comments')
    
    def __str__(self):
        return f"{self.user} {self.created_at}"
    