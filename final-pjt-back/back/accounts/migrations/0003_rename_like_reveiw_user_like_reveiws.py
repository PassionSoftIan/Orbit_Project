from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='like_reveiw',
            new_name='like_reveiws',
        ),
    ]
