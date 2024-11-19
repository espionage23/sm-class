# Generated by Django 5.1.3 on 2024-11-19 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('grade', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=10)),
                ('hobby', models.CharField(max_length=50)),
            ],
        ),
    ]
