# Generated by Django 5.0.3 on 2024-03-29 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product_code_alter_category_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='code',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
