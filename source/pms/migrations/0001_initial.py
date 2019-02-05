# Generated by Django 2.1.5 on 2019-02-05 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_charge_code', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Charge Code')),
                ('project_name', models.CharField(default=None, max_length=100, unique=True, verbose_name='Project Name')),
                ('client_name', models.CharField(default=None, max_length=100, verbose_name='Client Name')),
                ('client_department', models.CharField(default=None, max_length=100, verbose_name='Client Department')),
                ('client_phone', models.CharField(default=None, max_length=100, verbose_name='Client Phone')),
                ('project_total_hours', models.IntegerField(default=10, verbose_name='Total Hours')),
                ('project_comments', models.TextField(blank=True, max_length=25000, verbose_name='Comments')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ProjectTester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_hours', models.IntegerField(default=0, verbose_name='Assigned Hours')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pms.Projects')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TesterWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField(max_length=255, verbose_name='Task')),
                ('consumed_hours', models.IntegerField(default=0, verbose_name='Hours')),
                ('project_tester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pms.ProjectTester')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
