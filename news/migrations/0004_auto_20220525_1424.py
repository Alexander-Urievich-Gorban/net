# Generated by Django 3.2.13 on 2022-05-25 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20220525_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='my_value',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.BigIntegerField(default=0),
        ),
    ]
