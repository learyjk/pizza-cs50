# Generated by Django 2.2.7 on 2020-01-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20200109_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='title',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='additional',
            field=models.CharField(default='defaultoption', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='is_special',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='menu',
            field=models.CharField(default='defaultoption', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='size',
            field=models.CharField(default='defaultoption', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='style',
            field=models.CharField(default='deafultoption', max_length=64),
            preserve_default=False,
        ),
    ]
