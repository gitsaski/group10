# Generated by Django 4.2.6 on 2023-10-20 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0002_remove_job_text_job_application_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
