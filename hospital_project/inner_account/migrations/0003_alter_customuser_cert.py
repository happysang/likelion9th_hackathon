# Generated by Django 3.2.5 on 2021-07-29 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inner_account', '0002_remove_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cert',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]