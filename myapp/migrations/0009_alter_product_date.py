# Generated by Django 4.1.4 on 2023-01-01 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_product_delete_qan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2023, 1, 1, 22, 13, 53, 773864)),
        ),
    ]
