# Generated by Django 4.0.1 on 2022-01-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220127_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='code',
            field=models.CharField(max_length=36, unique=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='name',
            field=models.CharField(max_length=512, unique=True),
        ),
    ]