# Generated by Django 3.2.4 on 2021-06-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='title_tag', max_length=255),
        ),
    ]