# Generated by Django 3.0.2 on 2020-01-19 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_qrform'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrevent',
            name='feeamount',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qrform',
            name='noofmembers',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
