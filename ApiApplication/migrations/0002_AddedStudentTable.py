# Generated by Django 4.2.1 on 2023-06-01 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApplication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
