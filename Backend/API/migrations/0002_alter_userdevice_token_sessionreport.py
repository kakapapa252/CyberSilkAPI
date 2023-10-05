# Generated by Django 4.2.4 on 2023-08-06 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdevice',
            name='token',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='SessionReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('createDateTime', models.DateTimeField(auto_now_add=True)),
                ('userDevice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API.userdevice')),
            ],
        ),
    ]
