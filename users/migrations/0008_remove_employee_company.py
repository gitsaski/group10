# Generated by Django 4.2.6 on 2023-11-16 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_employee_company_employee_user_employer_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
    ]
