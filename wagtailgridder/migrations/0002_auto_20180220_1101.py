# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 16:01
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailgridder", "0001_squashed_0012_auto_20170607_1317"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gridindexpage",
            name="featured_description",
            field=wagtail.core.fields.RichTextField(
                blank=True,
                help_text="Text to be displayed below the hero image next to the featured items.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="gridindexpage",
            name="hero_description",
            field=wagtail.core.fields.RichTextField(
                blank=True,
                help_text="Text to be displayed beneath the logo over the background image.",
                null=True,
            ),
        ),
    ]
