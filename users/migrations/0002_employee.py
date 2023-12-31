# Generated by Django 4.2.6 on 2023-10-23 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
