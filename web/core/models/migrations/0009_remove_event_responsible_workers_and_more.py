# Generated by Django 4.2 on 2025-02-05 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0008_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='responsible_workers',
        ),
        migrations.AddField(
            model_name='event',
            name='responsible_worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsible_workers', to=settings.AUTH_USER_MODEL),
        ),
    ]
