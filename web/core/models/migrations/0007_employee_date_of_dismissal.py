# Generated by Django 4.2 on 2025-01-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_alter_calendarskip_date_until_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date_of_dismissal',
            field=models.DateField(blank=True, null=True),
        ),
    ]
