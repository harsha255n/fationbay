# Generated by Django 4.2.7 on 2024-02-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_alter_cart_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='sli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_imaga', models.ImageField(null=True, upload_to='images')),
                ('sl_imagb', models.ImageField(null=True, upload_to='images')),
                ('sl_imagc', models.ImageField(null=True, upload_to='images')),
            ],
        ),
    ]
