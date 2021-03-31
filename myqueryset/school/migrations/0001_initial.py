# Generated by Django 3.1.6 on 2021-03-31 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyStudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=500)),
                ('marks', models.IntegerField()),
                ('passing_year', models.DateField()),
            ],
        ),
    ]
