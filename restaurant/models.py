from django.db import models
from django.db.models import Avg
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
    average_rating = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    
    def __str__(self):
        return self.title
    def update_rating(self):
        average = Rating.objects.filter(menu_item=self).aggregate(Avg('rating'))['rating__avg']
        self.average_rating = average if average else 0
        self.save()
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.user.username} - {self.item.name} : {self.rating}"
    
    
class UserComments(models.Model):
    
    # ratings = (
    #     ( 1 , 'One Star'),
    #     ( 2 , 'Two Stars'),
    #     ( 3, 'Three Stars'),
    #     ( 4 , 'Four Stars'),
    #     ( 5 , 'Five Stars') 
    # )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=255)
    # rating = models.SmallIntegerField(default=1, choices=ratings)
    comment = models.TextField(max_length=8000)
    created_at = models.DateTimeField(default=timezone.now)
    helpful = models.BooleanField(default=False)
    reply_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, default=1, related_name='comments')
    
    def __str__(self):
        return f"{self.user} {self.created_at}"
    
    

class Cart(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, default=1, related_name='cart_items')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=1500)
    quantity = models.SmallIntegerField(null=True)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    class Meta:
        unique_together = ('item', 'user')
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='delivery_crew', null=True)
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    date = models.DateField(db_index=True)
    
    def __str__(self):
        return self.user
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(null=True)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        unique_together = ('order', 'item')
    def __str__(self):
        return self.item
    
    