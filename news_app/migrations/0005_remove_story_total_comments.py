# Generated by Django 3.2.6 on 2021-08-11 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0004_alter_comment_story_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='total_comments',
        ),
    ]
