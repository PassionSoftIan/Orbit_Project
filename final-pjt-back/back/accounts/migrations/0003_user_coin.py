# Generated by Django 3.2.18 on 2023-05-23 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='coin',
            field=models.IntegerField(default=0),
        ),
    ]
