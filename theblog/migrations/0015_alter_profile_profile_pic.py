# Generated by Django 3.2.4 on 2021-07-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_auto_20210723_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='theblog/images/default_pic.jpg', null=True, upload_to='images/profile/'),
        ),
    ]
