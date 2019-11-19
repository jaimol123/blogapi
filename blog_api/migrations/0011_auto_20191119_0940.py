# Generated by Django 2.2.6 on 2019-11-19 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0010_address_comments_newsletter_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Details'},
        ),
        migrations.RemoveField(
            model_name='comments',
            name='rating',
        ),
        migrations.AddField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='receipe_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rname', to='blog_api.Recipe'),
        ),
    ]