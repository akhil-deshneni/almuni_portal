# Generated by Django 4.1.6 on 2023-02-09 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0003_alter_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time_posted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]