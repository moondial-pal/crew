# Generated by Django 3.2.8 on 2021-10-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crew', '0002_auto_20211028_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='images',
            field=models.ImageField(blank=True, upload_to='crew/media/images/'),
        ),
    ]
