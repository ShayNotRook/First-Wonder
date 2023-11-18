# Generated by Django 4.2.7 on 2023-11-18 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0013_remove_usercomments_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1500)),
                ('active', models.BooleanField()),
                ('items', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='restaurant.menuitem')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
