# Generated by Django 2.0.7 on 2018-07-15 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='nid',
            field=models.IntegerField(default=2, max_length=6),
            preserve_default=False,
        ),
    ]