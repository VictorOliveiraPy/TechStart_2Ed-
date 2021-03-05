# Generated by Django 3.1.7 on 2021-03-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210305_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prince',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='Address',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='seller',
            name='state',
            field=models.CharField(max_length=30, verbose_name='Estado'),
        ),
    ]