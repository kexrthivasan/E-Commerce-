# Generated by Django 5.0.6 on 2024-06-23 15:52

import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_catagory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='image',
            field=models.ImageField(blank=True, default='20240623212138Dummy.png', null=True, upload_to=shop.models.getFileName),
        ),
    ]