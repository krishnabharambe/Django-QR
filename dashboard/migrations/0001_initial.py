# Generated by Django 3.0.2 on 2020-01-18 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QREvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10801)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=256)),
                ('disabledesc', models.CharField(max_length=256)),
            ],
        ),
    ]
