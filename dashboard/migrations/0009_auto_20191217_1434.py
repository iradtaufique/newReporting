# Generated by Django 2.2.2 on 2019-12-17 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_umuryango_kpi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='umuryango',
            name='achieved',
        ),
        migrations.RemoveField(
            model_name='umuryango',
            name='pending',
        ),
    ]
