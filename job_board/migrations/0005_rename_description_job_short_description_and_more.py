# Generated by Django 4.2.6 on 2023-11-07 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job_board', '0004_rename_date_added_job_date_posted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='description',
            new_name='short_description',
        ),
        migrations.AddField(
            model_name='job',
            name='long_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL),
        ),
    ]
