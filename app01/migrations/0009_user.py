# Generated by Django 2.0.7 on 2018-07-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20180715_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=64)),
            ],
        ),
    ]