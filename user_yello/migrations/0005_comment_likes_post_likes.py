# Generated by Django 4.1.1 on 2022-09-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_yello', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]