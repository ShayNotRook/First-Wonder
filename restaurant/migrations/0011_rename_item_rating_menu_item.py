# Generated by Django 4.2.7 on 2023-11-17 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_remove_usercomments_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='item',
            new_name='menu_item',
        ),
    ]
