# Generated by Django 3.2.3 on 2022-03-26 16:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexamapp', '0010_rename_coursedetail_questiondetail_coursename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveIntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('questionDetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineexamapp.questiondetail')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineexamapp.user')),
            ],
        ),
    ]
