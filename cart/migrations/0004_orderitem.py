# Generated by Django 2.2.7 on 2020-01-12 19:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20200109_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(max_length=16)),
                ('size', models.CharField(max_length=16)),
                ('style', models.CharField(max_length=64)),
                ('additional', models.CharField(max_length=255)),
                ('is_special', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('user_id', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Complete', 'Complete')], max_length=16)),
            ],
        ),
    ]
