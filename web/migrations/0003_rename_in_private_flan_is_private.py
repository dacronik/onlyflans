# Generated by Django 4.1.6 on 2023-08-03 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_flan_precio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flan',
            old_name='in_private',
            new_name='is_private',
        ),
    ]
