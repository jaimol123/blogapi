# Generated by Django 2.2.6 on 2019-11-05 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0027_auto_20191105_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
