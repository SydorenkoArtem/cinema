# Generated by Django 3.2.4 on 2021-07-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20210703_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='date_show',
            field=models.DateField(default='2021-06-28'),
            preserve_default=False,
        ),
    ]