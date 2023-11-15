# Generated by Django 4.2.7 on 2023-11-12 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0003_provider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='has_flat_price',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='price',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='service',
        ),
        migrations.AddField(
            model_name='provider',
            name='texto',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]