# Generated by Django 3.1.3 on 2021-03-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210326_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='mrp',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
