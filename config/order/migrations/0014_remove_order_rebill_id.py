# Generated by Django 4.2.2 on 2023-08-06 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_remove_confirmedcourse_price_with_discount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='rebill_id',
        ),
    ]
