# Generated by Django 2.2.9 on 2020-02-19 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_webcastpage_moderator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webcastpage',
            name='date',
            field=models.DateTimeField(help_text='The time of the event', verbose_name='Event time'),
        ),
    ]
