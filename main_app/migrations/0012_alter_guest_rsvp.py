# Generated by Django 3.2.9 on 2021-11-10 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_guest_rsvp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='rsvp',
            field=models.CharField(choices=[('Absolutely!', 'Absolutely!'), ('Not quite certain', 'Not quite certain'), ('Unfortunately, no...', 'Unfortunately, no...')], max_length=30),
        ),
    ]
