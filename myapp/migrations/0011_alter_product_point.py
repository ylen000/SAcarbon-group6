# Generated by Django 4.1.4 on 2023-01-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='point',
            field=models.CharField(max_length=500),
        ),
    ]