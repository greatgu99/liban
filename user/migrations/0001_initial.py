# Generated by Django 3.1.4 on 2022-09-25 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=200)),
                ('nickName', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('userId', models.CharField(max_length=200)),
                ('userImg', models.CharField(blank=True, max_length=200)),
                ('userDepartment', models.CharField(max_length=200)),
                ('authority', models.IntegerField()),
            ],
        ),
    ]