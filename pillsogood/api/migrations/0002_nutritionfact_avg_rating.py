# Generated by Django 3.2.9 on 2021-12-09 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutritionfact',
            name='avg_rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
