from django.apps import AppConfig


class CartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
    verbose_name = 'Система оплаты'
    verbose_name_plural = 'Система оплаты'
