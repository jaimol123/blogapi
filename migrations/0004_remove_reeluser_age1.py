# Generated by Django 2.2.6 on 2019-10-21 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20191021_0515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reeluser',
            name='age1',
        ),
    ]
