<<<<<<< HEAD
# Generated by Django 3.2.4 on 2021-07-28 17:21
=======
# Generated by Django 3.2.4 on 2021-07-28 15:26
>>>>>>> d035d2caa51afdb7a1a169c0cb2b1cd56a78f24c

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
            ],
        ),
    ]