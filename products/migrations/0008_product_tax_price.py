# Generated by Django 3.2 on 2023-06-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tax_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
