# Generated by Django 5.0.2 on 2024-02-23 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('product', '0004_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catergory',
            field=models.ForeignKey(choices=[], default=1, on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
            preserve_default=False,
        ),
    ]
