# Generated by Django 4.1.5 on 2023-05-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ByteApp', '0002_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=" ● 'description'. ● 'description'. ● 'description'. ", max_length=200),
        ),
    ]
