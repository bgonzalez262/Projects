# Generated by Django 3.0.4 on 2020-04-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vbc', '0002_auto_20200408_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='website',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
