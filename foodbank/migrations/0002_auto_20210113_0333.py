# Generated by Django 3.1.3 on 2021-01-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodbank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='lat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='branch',
            name='lng',
            field=models.IntegerField(default=0),
        ),
    ]
