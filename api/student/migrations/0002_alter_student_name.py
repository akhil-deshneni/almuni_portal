# Generated by Django 4.2.2 on 2023-06-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
