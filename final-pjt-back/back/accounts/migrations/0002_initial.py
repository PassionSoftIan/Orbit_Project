# Generated by Django 3.2.18 on 2023-05-23 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('movies', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_reveiw',
            field=models.ManyToManyField(related_name='liked_user', to='movies.Review'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
