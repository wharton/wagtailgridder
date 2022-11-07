# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-06 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields

try:
    from wagtail import blocks as core_blocks
    from wagtail import fields as core_fields
    from wagtail.documents import blocks as docs_blocks
except ImportError:
    from wagtail import blocks as core_blocks
    from wagtail import fields as core_fields
    from wagtail.documents import blocks as docs_blocks


class Migration(migrations.Migration):

    replaces = [
        ("wagtailgridder", "0001_initial"),
        ("wagtailgridder", "0002_griditem_landing_page_text"),
        ("wagtailgridder", "0003_remove_griditem_target_url"),
        ("wagtailgridder", "0004_auto_20161103_1446"),
        ("wagtailgridder", "0005_auto_20161117_0715"),
        ("wagtailgridder", "0006_auto_20170217_1354"),
        ("wagtailgridder", "0007_auto_20170217_1404"),
        ("wagtailgridder", "0008_auto_20170320_1707"),
        ("wagtailgridder", "0009_gridindexpage_logo_image"),
        ("wagtailgridder", "0010_auto_20170403_1347"),
        ("wagtailgridder", "0011_auto_20170404_1454"),
        ("wagtailgridder", "0012_auto_20170607_1317"),
    ]

    initial = True

    dependencies = [
        ("wagtailimages", "0018_remove_rendition_filter"),
        ("taggit", "0002_auto_20150616_2121"),
        ("wagtailimages", "0013_make_rendition_upload_callable"),
        ("wagtailcore", "0029_unicode_slugfield_dj19"),
    ]

    operations = [
        migrations.CreateModel(
            name="GridCategory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
            options={"verbose_name_plural": "grid categories",},
        ),
        migrations.CreateModel(
            name="GridIndexGridItemRelationship",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False,},
        ),
        migrations.CreateModel(
            name="GridIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
            ],
            options={"verbose_name": "Grid Index Page",},
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="GridItem",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "summary",
                    core_fields.RichTextField(
                        default="",
                        help_text='The summary will appear in the item "card" view.',
                        verbose_name="Summary",
                    ),
                ),
                (
                    "full_desc",
                    core_fields.RichTextField(
                        default="",
                        help_text="The description will appear when the grid item is clicked and expanded.",
                        verbose_name="Full Description",
                    ),
                ),
                (
                    "target_url",
                    models.URLField(
                        blank=True,
                        default="",
                        help_text="The URL for this grid item, if it is not a full Django App.",
                        verbose_name="URL",
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(null=True, verbose_name="Page Modified"),
                ),
                (
                    "buttons",
                    core_fields.StreamField(
                        (
                            (
                                "button_section",
                                core_blocks.StructBlock(
                                    (
                                        (
                                            "action_items",
                                            core_blocks.StreamBlock(
                                                (
                                                    (
                                                        "document_button",
                                                        core_blocks.StructBlock(
                                                            (
                                                                (
                                                                    "label",
                                                                    core_blocks.TextBlock(
                                                                        required=True
                                                                    ),
                                                                ),
                                                                (
                                                                    "document",
                                                                    docs_blocks.DocumentChooserBlock(
                                                                        required=True
                                                                    ),
                                                                ),
                                                            ),
                                                            icon="fa-file",
                                                        ),
                                                    ),
                                                    (
                                                        "url_button",
                                                        core_blocks.StructBlock(
                                                            (
                                                                (
                                                                    "label",
                                                                    core_blocks.TextBlock(
                                                                        required=True
                                                                    ),
                                                                ),
                                                                (
                                                                    "url",
                                                                    core_blocks.URLBlock(
                                                                        required=True
                                                                    ),
                                                                ),
                                                            ),
                                                            icon="fa-link",
                                                        ),
                                                    ),
                                                    (
                                                        "placeholder",
                                                        core_blocks.StructBlock(
                                                            (), icon="fa-square-o"
                                                        ),
                                                    ),
                                                ),
                                                help_text="A button or URL within a button section.",
                                            ),
                                        ),
                                    )
                                ),
                            ),
                        ),
                        null=True,
                    ),
                ),
                (
                    "main_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                    ),
                ),
                (
                    "small_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                    ),
                ),
            ],
            options={"verbose_name": "Grid Item",},
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="GridItemTag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="wagtailgridder.GridItem",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wagtailgridder_griditemtag_items",
                        to="taggit.Tag",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.AddField(
            model_name="griditem",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="wagtailgridder.GridItemTag",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AddField(
            model_name="gridindexgriditemrelationship",
            name="grid_relationship",
            field=modelcluster.fields.ParentalKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="grid_index_grid_item_relationship",
                to="wagtailgridder.GridIndexPage",
            ),
        ),
        migrations.AddField(
            model_name="gridindexgriditemrelationship",
            name="grid_item",
            field=models.ForeignKey(
                help_text="Add a grid item to the page",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="wagtailgridder.GridItem",
                verbose_name="Grid Items",
            ),
        ),
        migrations.AddField(
            model_name="griditem",
            name="landing_page_text",
            field=core_fields.RichTextField(
                blank=True,
                help_text="This is the text which will appear on the grid item's landing page.",
                null=True,
                verbose_name="Landing Page Text",
            ),
        ),
        migrations.RemoveField(model_name="griditem", name="target_url",),
        migrations.RenameField(
            model_name="griditem", old_name="main_image", new_name="description_image",
        ),
        migrations.RenameField(
            model_name="griditem", old_name="full_desc", new_name="description_text",
        ),
        migrations.RenameField(
            model_name="griditem", old_name="small_image", new_name="summary_image",
        ),
        migrations.RenameField(
            model_name="griditem", old_name="summary", new_name="summary_text",
        ),
        migrations.AlterField(
            model_name="griditem",
            name="buttons",
            field=core_fields.StreamField(
                (
                    (
                        "button_section",
                        core_blocks.StructBlock(
                            (
                                (
                                    "action_items",
                                    core_blocks.StreamBlock(
                                        (
                                            (
                                                "document_button",
                                                core_blocks.StructBlock(
                                                    (
                                                        (
                                                            "label",
                                                            core_blocks.TextBlock(
                                                                required=True
                                                            ),
                                                        ),
                                                        (
                                                            "document",
                                                            docs_blocks.DocumentChooserBlock(
                                                                required=True
                                                            ),
                                                        ),
                                                    ),
                                                    icon="fa-file",
                                                ),
                                            ),
                                            (
                                                "url_button",
                                                core_blocks.StructBlock(
                                                    (
                                                        (
                                                            "label",
                                                            core_blocks.TextBlock(
                                                                required=True
                                                            ),
                                                        ),
                                                        (
                                                            "url",
                                                            core_blocks.TextBlock(
                                                                required=True
                                                            ),
                                                        ),
                                                    ),
                                                    icon="fa-link",
                                                ),
                                            ),
                                            (
                                                "placeholder",
                                                core_blocks.StructBlock(
                                                    (), icon="fa-square-o"
                                                ),
                                            ),
                                        ),
                                        help_text="A button or URL within a button section.",
                                    ),
                                ),
                            )
                        ),
                    ),
                ),
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="griditem",
            name="categories",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True, to="wagtailgridder.GridCategory"
            ),
        ),
        migrations.AddField(
            model_name="gridindexpage",
            name="featured_grid_item_1",
            field=models.ForeignKey(
                blank=True,
                help_text="First featured grid item underneath the hero image.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailgridder.GridItem",
                verbose_name="Featured Item One",
            ),
        ),
        migrations.AddField(
            model_name="gridindexpage",
            name="featured_grid_item_2",
            field=models.ForeignKey(
                blank=True,
                help_text="Second featured grid item underneath the hero image.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailgridder.GridItem",
                verbose_name="Featured Item Two,",
            ),
        ),
        migrations.AddField(
            model_name="gridindexpage",
            name="hero_background_image",
            field=models.ForeignKey(
                blank=True,
                help_text="The background image for the hero section. This triggers the section to be displayed if an image is selected.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.Image",
            ),
        ),
        migrations.AddField(
            model_name="gridindexpage",
            name="hero_logo_image",
            field=models.ForeignKey(
                blank=True,
                help_text="The logo image to be displayed over the background image.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.Image",
            ),
        ),
        migrations.AddField(
            model_name="gridindexpage",
            name="featured_description",
            field=models.TextField(
                blank=True,
                help_text="Text to be displayed below the hero image next to the featured items.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="gridindexpage",
            name="hero_button_text",
            field=models.CharField(
                blank=True,
                help_text="Text for the call-to-action button beneath the text and logo over the background image.",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="gridindexpage",
            name="hero_button_url",
            field=models.CharField(
                blank=True,
                help_text="URL for the call-to-action button beneath the text and logo over the background image.",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="gridindexpage",
            name="hero_description",
            field=models.TextField(
                blank=True,
                help_text="Text to be displayed beneath the logo over the background image.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="griditem",
            name="description_video",
            field=models.URLField(
                blank=True,
                help_text="This video will be embedded in the expanded area when populated.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="griditem",
            name="description_image",
            field=models.ForeignKey(
                blank=True,
                help_text="This image will appear in the expanded area when populated.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.Image",
            ),
        ),
        migrations.AlterField(
            model_name="griditem",
            name="description_text",
            field=core_fields.RichTextField(
                blank=True,
                help_text="This description will appear in the expanded area when populated.",
                null=True,
                verbose_name="Full Description",
            ),
        ),
    ]
