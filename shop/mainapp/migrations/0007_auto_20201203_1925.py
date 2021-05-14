# Generated by Django 3.1.2 on 2020-12-03 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20201201_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='for_anonymous_user',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='in_order',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона'),
        ),
    ]
