# Generated by Django 3.0.8 on 2020-11-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201110_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dark_mode',
            field=models.BooleanField(default=True),
        ),
    ]
