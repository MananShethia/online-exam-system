# Generated by Django 3.2.3 on 2022-03-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexamapp', '0012_facultycourses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultycourses',
            name='facultyCourse',
            field=models.CharField(choices=[('Computer Engineering', 'Computer Engineering'), ('Mechanical', 'Mechanical'), ('Civil Engineering', 'Civil Engineering'), ('Electrical', 'Electrical')], max_length=100),
        ),
    ]