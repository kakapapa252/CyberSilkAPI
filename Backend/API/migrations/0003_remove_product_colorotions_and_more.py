# Generated by Django 4.2.4 on 2023-10-05 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_userdevice_token_sessionreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colorOtions',
        ),
        migrations.RemoveField(
            model_name='product',
            name='phoneTypeOptions',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sizeOptions',
        ),
        migrations.AddField(
            model_name='product',
            name='colorOtions',
            field=models.ManyToManyField(to='API.coloroptions'),
        ),
        migrations.AddField(
            model_name='product',
            name='phoneTypeOptions',
            field=models.ManyToManyField(to='API.phonetypeoptions'),
        ),
        migrations.AddField(
            model_name='product',
            name='sizeOptions',
            field=models.ManyToManyField(to='API.sizeoptions'),
        ),
    ]
