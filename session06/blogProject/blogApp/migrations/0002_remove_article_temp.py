# Generated by Django 4.0.3 on 2022-03-31 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='temp',
        ),
    ]
