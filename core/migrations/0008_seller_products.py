# Generated by Django 3.1.7 on 2021-03-04 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210304_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='products',
            field=models.ManyToManyField(related_name='products', to='core.Product'),
        ),
    ]
