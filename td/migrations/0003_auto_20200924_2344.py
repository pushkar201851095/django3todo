# Generated by Django 3.0.7 on 2020-09-24 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('td', '0002_auto_20200923_2136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='importanat',
            new_name='important',
        ),
    ]
