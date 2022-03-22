# Generated by Django 3.2.3 on 2022-03-22 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexamapp', '0005_user_profilepic'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=100)),
                ('facultyDetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineexamapp.user')),
            ],
        ),
    ]
