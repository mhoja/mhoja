# Generated by Django 3.2.4 on 2021-06-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0003_auto_20210612_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
