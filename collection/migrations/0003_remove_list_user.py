# Generated by Django 2.0.10 on 2019-11-12 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_list_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='user',
        ),
    ]