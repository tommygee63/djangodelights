# Generated by Django 4.1.7 on 2023-03-11 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_rename_muenu_item_purachase_menu_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Purachase',
            new_name='Purchase',
        ),
    ]
