# Generated by Django 2.0.2 on 2018-04-24 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0005_auto_20180424_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisepage',
            name='cover_sheet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
    ]
