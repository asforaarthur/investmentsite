# Generated by Django 4.2.7 on 2023-11-12 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0005_investment_texto_delete_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='texto',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]
