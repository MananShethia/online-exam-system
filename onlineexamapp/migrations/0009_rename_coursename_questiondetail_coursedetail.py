# Generated by Django 3.2.3 on 2022-03-26 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexamapp', '0008_questiondetail_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questiondetail',
            old_name='courseName',
            new_name='courseDetail',
        ),
    ]