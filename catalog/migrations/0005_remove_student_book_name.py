# Generated by Django 2.2.2 on 2019-06-21 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20190621_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='book_name',
        ),
    ]
