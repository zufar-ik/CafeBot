# Generated by Django 4.0.4 on 2022-04-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_about1_category_anons_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name', 'slug', 'anons', 'image', 'price']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category']},
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]