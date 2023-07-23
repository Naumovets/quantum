# Generated by Django 4.2.2 on 2023-07-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_orderitem_create_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='create_date',
            field=models.DateField(verbose_name='Куплен'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='end_date',
            field=models.DateField(verbose_name='Окончание'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price_with_discount',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True, verbose_name='Цена со скидкой'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='update_date',
            field=models.DateField(verbose_name='Продлен'),
        ),
    ]