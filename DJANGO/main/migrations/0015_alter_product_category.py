# Generated by Django 4.0.4 on 2022-05-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('💫 РАМАДАН СЕТ', '💫 РАМАДАН СЕТ'), ('🍳 Сеты на завтрак', '🍳 Сеты на завтрак'), ('🍔🍟🥤 Сеты', '🍔🍟🥤 Сеты'), ('🍔 Стандартные бургеры', '🍔 Стандартные бургеры'), ('🍔 Премиум бургеры', '🍔 Премиум бургеры'), ('🍗 Куриные блюда', '🍗 Куриные блюда'), ('🧀 Соусы', '🧀 Соусы'), ('🍟 Снеки', '🍟 Снеки'), ('🥗 Салаты', '🥗 Салаты'), ('🍰 Десерты', '🍰 Десерты'), ('☕ Горячие напитки', '☕ Горячие напитки'), ('🧋 Холодные напитки', '🧋 Холодные напитки'), ('🥤 Классические напитки', '🥤 Классические напитки'), ('Русский язык', 'Русский язык')], max_length=250),
        ),
    ]
