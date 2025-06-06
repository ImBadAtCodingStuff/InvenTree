# Generated by Django 4.2.18 on 2025-01-20 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0053_alter_build_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='start_date',
            field=models.DateField(blank=True, help_text='Scheduled start date for this build order', null=True, verbose_name='Build start date'),
        ),
    ]
