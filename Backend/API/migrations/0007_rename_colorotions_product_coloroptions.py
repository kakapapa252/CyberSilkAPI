# Generated by Django 4.2.4 on 2023-10-05 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_phonetypeoptions_modelcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='colorOtions',
            new_name='colorOptions',
        ),
    ]
