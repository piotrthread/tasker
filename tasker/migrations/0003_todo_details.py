# Generated by Django 2.2.1 on 2019-05-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0002_auto_20190521_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='details',
            field=models.CharField(max_length=256, null=True),
        ),
    ]