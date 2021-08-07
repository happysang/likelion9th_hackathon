# Generated by Django 3.2.4 on 2021-08-04 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inner_account', '0003_auto_20210804_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]