# Generated by Django 4.2.6 on 2023-12-10 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20231209_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='contact_number',
            new_name='phone_number',
        ),
    ]
