# Generated by Django 3.2.13 on 2022-04-13 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctions',
            name='image',
            field=models.CharField(max_length=256, verbose_name='图片url'),
        ),
    ]