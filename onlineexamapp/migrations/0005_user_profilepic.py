# Generated by Django 3.2.3 on 2022-03-18 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexamapp', '0004_user_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profilePic',
            field=models.ImageField(default='', upload_to='profilePic/'),
        ),
    ]
