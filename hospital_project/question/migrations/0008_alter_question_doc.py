# Generated by Django 3.2.5 on 2021-08-13 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0007_alter_qcomment_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='doc',
            field=models.CharField(max_length=20, null=True),
        ),
    ]