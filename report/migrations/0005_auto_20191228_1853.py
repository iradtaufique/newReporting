# Generated by Django 3.0.1 on 2019-12-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20191228_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporttype',
            name='deadline',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
