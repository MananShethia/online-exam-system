# Generated by Django 3.2.3 on 2022-03-18 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexamapp', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userStatus',
            field=models.CharField(default='Pending', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='userType',
            field=models.CharField(default='Student', max_length=100),
        ),
    ]
