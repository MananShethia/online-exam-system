# Generated by Django 3.2.3 on 2022-03-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexamapp', '0007_questiondetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiondetail',
            name='question',
            field=models.TextField(default=''),
        ),
    ]
