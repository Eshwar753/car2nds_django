# Generated by Django 5.0 on 2023-12-20 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_team_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='photos/%m/%Y/'),
        ),
    ]
