# Generated by Django 3.2.13 on 2022-05-25 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20220525_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='my_value',
        ),
    ]
