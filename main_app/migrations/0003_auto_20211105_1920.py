# Generated by Django 3.2.9 on 2021-11-05 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_post_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Test name', max_length=150),
        ),
    ]