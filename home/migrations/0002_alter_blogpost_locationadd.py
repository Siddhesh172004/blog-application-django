# Generated by Django 4.0.2 on 2023-01-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='locationadd',
            field=models.CharField(blank=True, default='some_value', max_length=1000),
        ),
    ]
