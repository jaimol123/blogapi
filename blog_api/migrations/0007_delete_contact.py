# Generated by Django 2.2.6 on 2019-11-18 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0006_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]