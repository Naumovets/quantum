# Generated by Django 4.2.2 on 2023-07-23 17:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0002_alter_cart_options_alter_cartitem_options_and_more'),
        ('course', '0011_fileofwebinar_title'),
        ('order', '0009_rename_full_price_order_result_price_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderCourse',
            new_name='ConfirmedCourse',
        ),
        migrations.AlterModelOptions(
            name='confirmedcourse',
            options={'verbose_name': 'Курс пользователя', 'verbose_name_plural': 'Курсы пользователей'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ пользователя', 'verbose_name_plural': 'Заказы пользователей'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='period',
            field=models.CharField(choices=[('FL', 'Полный'), ('MN', 'Месячный')], max_length=2, verbose_name='Период'),
        ),
    ]