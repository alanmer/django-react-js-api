# Generated by Django 4.2 on 2023-04-25 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
