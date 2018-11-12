# Generated by Django 2.0.7 on 2018-11-12 15:29

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0002_auto_20181112_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counties', models.CharField(max_length=25)),
                ('codes', models.IntegerField()),
                ('cty_code', models.CharField(max_length=24)),
                ('dis', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
