# Generated by Django 4.0.4 on 2022-05-02 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tg_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
