# Generated by Django 2.2 on 2019-04-27 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('Honey moon suites', 'Honey moon suites'), ('Master', 'Master'), ('Executive Suite', 'Executive Suite'), ('Superior Rooms', 'Superior Rooms'), ('Ambassadorial Rooms', 'Ambassadorial Rooms'), ('Standard Rooms', 'Standard Rooms')], default='Master', max_length=100)),
                ('price', models.IntegerField()),
                ('room_number', models.IntegerField()),
                ('no_bed', models.IntegerField()),
                ('is_booked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('ratings', models.IntegerField()),
                ('meals', models.ManyToManyField(blank=True, related_name='hotel', to='hotel.Meal')),
                ('rooms', models.ManyToManyField(blank=True, related_name='rooms', to='hotel.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_created=True)),
                ('end_date', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
