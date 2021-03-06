# Generated by Django 3.0.4 on 2020-04-08 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.IntegerField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=200)),
                ('website', models.CharField(blank=True, max_length=300, null=True)),
                ('about', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
