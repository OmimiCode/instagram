# Generated by Django 3.2 on 2021-05-20 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostForm',
            new_name='Post',
        ),
    ]
