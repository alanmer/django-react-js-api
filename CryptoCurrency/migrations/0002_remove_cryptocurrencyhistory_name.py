# Generated by Django 4.2 on 2023-04-25 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CryptoCurrency', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cryptocurrencyhistory',
            name='name',
        ),
    ]