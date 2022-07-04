# Generated by Django 3.2.12 on 2022-07-04 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reports', '0010_incidentreport_case_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, default='')),
                ('context', models.JSONField(blank=True, default=dict)),
                ('authorities', models.ManyToManyField(related_name='cases', to='accounts.Authority')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cases', to='reports.incidentreport')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StatusTemplate',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('definition', models.JSONField()),
                ('is_default', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StatusTemplateMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('report_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.reporttype')),
                ('status_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.statustemplate')),
            ],
        ),
        migrations.CreateModel(
            name='StatusHistory',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, default='')),
                ('data', models.JSONField(blank=True, default=dict)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.case')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CaseDefinition',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('condition', models.TextField()),
                ('report_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.reporttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='case',
            name='status_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cases.statustemplate'),
        ),
        migrations.AddConstraint(
            model_name='statustemplatemapping',
            constraint=models.UniqueConstraint(fields=('status_template', 'report_type'), name='case_status_template_unique_ids'),
        ),
    ]
