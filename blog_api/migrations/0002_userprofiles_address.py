# Generated by Django 2.2.6 on 2019-11-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
