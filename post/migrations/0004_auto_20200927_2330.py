# Generated by Django 2.2.14 on 2020-09-27 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20200927_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name Surname'),
        ),
    ]
