# Generated by Django 3.2.13 on 2022-04-19 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='商品名称')),
                ('name', models.CharField(max_length=128, verbose_name='用户')),
                ('content', models.CharField(max_length=512, verbose_name='用户')),
            ],
        ),
    ]
