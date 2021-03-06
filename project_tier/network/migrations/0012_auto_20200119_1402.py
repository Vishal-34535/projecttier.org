# Generated by Django 2.1.15 on 2020-01-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_personcategory_tier_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='fellowship_year',
            field=models.IntegerField(blank=True, choices=[(2010, '2010–2011'), (2011, '2011–2012'), (2012, '2012–2013'), (2013, '2013–2014'), (2014, '2014–2015'), (2015, '2015–2016'), (2016, '2016–2017'), (2017, '2017–2018'), (2018, '2018–2019'), (2019, '2019–2020'), (2020, '2020–2021')], null=True),
        ),
    ]
