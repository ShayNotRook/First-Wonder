# Generated by Django 4.2.7 on 2023-11-17 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0012_usercomments_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercomments',
            name='rating',
        ),
    ]
