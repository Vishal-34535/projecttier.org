# Generated by Django 2.2.9 on 2020-05-18 20:54

from django.db import migrations
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('course_materials', '0003_coursematerialsindexpage_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialspage',
            name='course_level_tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='uuid_e4b20ecd_f0d6_488d_a1f3_ad9e47f28a35', through='course_materials.CourseLevelTag', to='taggit.Tag', verbose_name='course level tags'),
        ),
        migrations.AlterField(
            model_name='coursematerialspage',
            name='discipline_tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='uuid_d3e86784_844d_426a_ad8b_df78d89fdd3d', through='course_materials.DisciplineTag', to='taggit.Tag', verbose_name='discipline tags'),
        ),
        migrations.AlterField(
            model_name='coursematerialspage',
            name='protocol_tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='uuid_f8d1b914_e5e2_4a84_a059_36c26ab23e54', through='course_materials.ProtocolTag', to='taggit.Tag', verbose_name='protocol tags'),
        ),
    ]
