# Generated by Django 3.0.4 on 2020-03-10 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]