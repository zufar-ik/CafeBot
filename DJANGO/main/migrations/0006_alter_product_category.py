# Generated by Django 4.0.4 on 2022-04-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('💫 РАМАДАН СЕТ', '💫 РАМАДАН СЕТ'), ('🍳 Сеты на завтрак', '🍳 Сеты на завтрак'), ('🍔🍟🥤 Сеты', '🍔🍟🥤 Сеты'), ('🍔 Стандартные бургеры', '🍔 Стандартные бургеры'), ('🍔 Премиум бургеры', '🍔 Премиум бургеры'), ('🍗 Куриные блюда', '🍗 Куриные блюда'), ('🧀 Соусы', '🧀 Соусы'), ('🍟 Снеки', '🍟 Снеки'), ('🥗 Салаты', '🥗 Салаты'), ('🍰 Десерты', '🍰 Десерты'), ('☕ Горячие напитки', '☕ Горячие напитки'), ('🧋 Холодные напитки', '🧋 Холодные напитки'), ('🥤 Классические напитки', '🥤 Классические напитки')], max_length=250),
        ),
    ]
