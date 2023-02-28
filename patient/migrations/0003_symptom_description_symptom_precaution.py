# Generated by Django 3.2.7 on 2022-06-07 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20220607_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom_Description',
            fields=[
                ('Disease', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('Description', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom_Precaution',
            fields=[
                ('Disease', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('Precaution_1', models.CharField(max_length=255)),
                ('Precaution_2', models.CharField(max_length=255)),
                ('Precaution_3', models.CharField(max_length=255)),
                ('Precaution_4', models.CharField(max_length=255)),
            ],
        ),
    ]
