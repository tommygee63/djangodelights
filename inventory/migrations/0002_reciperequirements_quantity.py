# Generated by Django 4.1.7 on 2023-03-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciperequirements',
            name='quantity',
            field=models.FloatField(default=0),
        ),
    ]
