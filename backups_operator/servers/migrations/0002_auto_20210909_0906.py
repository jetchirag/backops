# Generated by Django 3.1.13 on 2021-09-09 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='client_version',
        ),
        migrations.RemoveField(
            model_name='server',
            name='hetzner_id',
        ),
    ]
