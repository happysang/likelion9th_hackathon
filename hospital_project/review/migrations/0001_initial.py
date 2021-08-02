# Generated by Django 3.2.5 on 2021-08-03 04:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('hname', models.CharField(max_length=20)),
                ('dname', models.CharField(max_length=10)),
                ('dept', models.CharField(max_length=20)),
                ('body', models.TextField(max_length=300)),
                ('cert', models.ImageField(blank=True, null=True, upload_to='review/%y/%m/%d')),
                ('like', models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
