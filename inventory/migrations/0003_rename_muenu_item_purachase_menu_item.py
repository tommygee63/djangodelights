# Generated by Django 4.1.7 on 2023-03-08 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_reciperequirements_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purachase',
            old_name='muenu_item',
            new_name='menu_item',
        ),
    ]
