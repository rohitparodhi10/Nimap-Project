# Generated by Django 5.1.1 on 2024-09-12 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_client_created_by_alter_project_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='client',
        ),
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='project',
            name='users',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
