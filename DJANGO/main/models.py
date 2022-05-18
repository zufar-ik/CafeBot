from django.db import models

class Users(models.Model):
    objects = None
    tg_id = models.IntegerField()
    username = models.CharField(max_length=50, null=True)
    lname = models.CharField(max_length=150)


class Product(models.Model):
    objects = None
    CHOISE = [
        ('💫 РАМАДАН СЕТ', '💫 РАМАДАН СЕТ'),
        ('🍳 Сеты на завтрак', '🍳 Сеты на завтрак'),
        ('🍔🍟🥤 Сеты', '🍔🍟🥤 Сеты'),
        ('🍔 Стандартные бургеры', '🍔 Стандартные бургеры'),
        ('🍔 Премиум бургеры', '🍔 Премиум бургеры'),
        ('🍗 Куриные блюда', '🍗 Куриные блюда'),
        ('🧀 Соусы', '🧀 Соусы'),
        ('🍟 Снеки', '🍟 Снеки'),
        ('🥗 Салаты', '🥗 Салаты'),
        ('🍰 Десерты', '🍰 Десерты'),
        ('☕ Горячие напитки', '☕ Горячие напитки'),
        ('🧋 Холодные напитки', '🧋 Холодные напитки'),
        ('🥤 Классические напитки', '🥤 Классические напитки')

    ]
    category = models.CharField(max_length=250, choices=CHOISE)
    title = models.TextField(default='Скоро мы сюда добавим блюда!')

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.category


class Category(models.Model):
    clas = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='choise')
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    anons = models.TextField()
    image = models.FileField(upload_to='images/')
    price = models.CharField(max_length=150)
    class Meta:
        ordering = [
            'name',
            'slug',
            'anons',
            'image',
            'price', ]

    def __str__(self):
        return self.name


class Cart(models.Model):
    tg_id = models.IntegerField()
    name = models.TextField()
    quantity = models.IntegerField()
    price = models.TextField()

    def __str__(self):
        return self.name