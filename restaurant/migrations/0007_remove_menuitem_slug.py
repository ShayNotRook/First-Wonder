# Generated by Django 4.2.7 on 2023-11-13 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_category_menuitem_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='slug',
        ),
    ]