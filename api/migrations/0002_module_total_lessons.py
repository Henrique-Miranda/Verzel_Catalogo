# Generated by Django 3.2 on 2022-01-09 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='total_lessons',
            field=models.IntegerField(default=1),
        ),
    ]
