# Generated by Django 4.2.7 on 2024-01-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
