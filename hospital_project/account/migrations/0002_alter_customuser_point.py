# Generated by Django 3.2.5 on 2021-07-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='point',
            field=models.IntegerField(null=True),
        ),
    ]
