# Generated by Django 4.1.4 on 2022-12-22 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='cname',
        ),
    ]