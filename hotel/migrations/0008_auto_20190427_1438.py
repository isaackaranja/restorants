# Generated by Django 2.2 on 2019-04-27 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_auto_20190427_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='book',
            new_name='is_booked',
        ),
    ]
