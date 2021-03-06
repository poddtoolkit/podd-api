# Generated by Django 3.2.12 on 2022-03-23 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_authorityuser_managers_remove_authority_domain_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('key', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
