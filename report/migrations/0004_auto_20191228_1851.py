# Generated by Django 3.0.1 on 2019-12-28 18:51

from django.db import migrations, models
import report.models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20191228_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporttype',
            name='deadline',
            field=models.DateTimeField(default=report.models.geting_date),
        ),
    ]
