# Generated by Django 2.0.10 on 2019-12-29 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0007_item_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]