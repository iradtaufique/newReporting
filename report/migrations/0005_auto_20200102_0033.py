# Generated by Django 3.0.2 on 2020-01-02 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20200101_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_file',
            field=models.FileField(upload_to='reports'),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportType'),
        ),
        migrations.AlterField(
            model_name='report',
            name='submitted_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
