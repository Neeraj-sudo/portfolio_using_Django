# Generated by Django 3.0.3 on 2020-11-25 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0004_auto_20201124_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='profile_pic',
            field=models.FilePathField(path='/img'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/img'),
        ),
    ]
