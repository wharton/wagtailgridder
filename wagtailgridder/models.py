from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils import timezone

from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    PageChooserPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from .blocks import ButtonBlock
from .settings import get_grid_item_parent_page_types, get_grid_index_page_subpage_types


class GridItemTag(TaggedItemBase):
    """
    Object to hold existing tags for Grid Items.
    """

    content_object = ParentalKey(
        "GridItem",
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )


class GridCategory(models.Model):
    """
    Categories which a grid item can belong to. A grid item can belong to many
    categories. Categories can be selected from the top of the grid index page.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "grid categories"


class GridItem(Page):
    """
    The fields needed to properly display a grid item.
    The template will omit any fields not included automagically.
    """

    parent_page_types = get_grid_item_parent_page_types()

    class Meta:
        verbose_name = "Grid Item"

    summary_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    summary_text = RichTextField(
        "Summary",
        default="",
        help_text='The summary will appear in the item "card" view.',
    )
    description_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="This image will appear in the expanded area when populated.",
    )
    description_text = RichTextField(
        "Full Description",
        null=True,
        blank=True,
        help_text="This description will appear in the expanded area when populated.",
    )
    description_video = models.URLField(
        null=True,
        blank=True,
        help_text="This video will be embedded in the expanded area when populated.",
    )
    landing_page_text = RichTextField(
        "Landing Page Text",
        null=True,
        blank=True,
        help_text="This is the text which will appear on the grid item's landing page.",
    )
    buttons = StreamField(ButtonBlock(), null=True)
    tags = ClusterTaggableManager(through=GridItemTag, blank=True)
    categories = ParentalManyToManyField("GridCategory", blank=True)
    modified = models.DateTimeField("Page Modified", null=True)

    search_fields = Page.search_fields + [
        index.SearchField("summary_text"),
        index.SearchField("description_text"),
        index.SearchField("landing_page_text"),
    ]

    CARD_PANELS = [
        ImageChooserPanel("summary_image"),
        FieldPanel("summary_text"),
    ]

    DETAIL_PANELS = [
        ImageChooserPanel("description_image"),
        FieldPanel("description_text"),
        FieldPanel("description_video"),
        FieldPanel("landing_page_text"),
    ]

    META_PANELS = [
        FieldPanel("tags"),
        FieldPanel("categories", widget=CheckboxSelectMultiple),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            CARD_PANELS,
            heading="Card Information",
            classname="collapsible",
        ),
        MultiFieldPanel(
            DETAIL_PANELS,
            heading="Expanded Description & Page Information",
            classname="collapsible",
        ),
        StreamFieldPanel(
            "buttons",
        ),
        MultiFieldPanel(
            META_PANELS,
            heading="Metadata",
            classname="collapsible",
        ),
    ]

    def save(self, *args, **kwargs):
        self.modified = timezone.now()
        super(GridItem, self).save(*args, **kwargs)


class GridIndexGridItemRelationship(Orderable, models.Model):
    """
    Allows the content creator to associate Grid Items on a
    Grid Index Page.
    """

    grid_relationship = ParentalKey(
        "GridIndexPage",
        related_name="grid_index_grid_item_relationship",
        on_delete=models.CASCADE,
    )
    grid_item = models.ForeignKey(
        "GridItem",
        related_name="+",
        help_text="Add a grid item to the page",
        verbose_name="Grid Items",
        on_delete=models.CASCADE,
    )
    panels = [PageChooserPanel("grid_item")]


class GridIndexPageAbstract(models.Model):
    """
    Index page for Grid Items.
    This links the grid items to the categories and provides a page to display them on.

    This abstract class exists to allow compositing the index page with other page
    functionality by future users. GridIndexPage below makes this concrete.
    """

    subpage_types = get_grid_index_page_subpage_types()

    hero_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="The background image for the hero section. This triggers the "
        "section to be displayed if an image is selected.",
    )

    hero_logo_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="The logo image to be displayed over the background image.",
    )

    hero_description = RichTextField(
        null=True,
        blank=True,
        help_text="Text to be displayed beneath the logo over the background image.",
    )

    hero_button_text = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text="Text for the call-to-action button beneath the text and logo over "
        "the background image.",
    )

    hero_button_url = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text="URL for the call-to-action button beneath the text and logo over "
        "the background image.",
    )

    featured_description = RichTextField(
        null=True,
        blank=True,
        help_text="Text to be displayed below the hero image next to the featured "
        "items.",
    )

    featured_grid_item_1 = models.ForeignKey(
        GridItem,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="First featured grid item underneath the hero image.",
        verbose_name="Featured Item One",
    )

    featured_grid_item_2 = models.ForeignKey(
        GridItem,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Second featured grid item underneath the hero image.",
        verbose_name="Featured Item Two,",
    )

    @property
    def grid_items(self):
        grid_items = [n.grid_item for n in self.grid_index_grid_item_relationship.all()]
        return grid_items

    @property
    def categories(self):
        grid_item_categories = (
            GridIndexGridItemRelationship.objects.values_list(
                "grid_item__categories__name"
            )
            .filter(
                grid_relationship__id=self.id,
            )
            .order_by(
                "grid_item__categories__name",
            )
            .distinct()
        )

        categories = []

        for gic in grid_item_categories:
            if gic[0] is not None:
                categories.append(gic[0])

        return categories

    HERO_PANELS = [
        ImageChooserPanel("hero_background_image"),
        ImageChooserPanel("hero_logo_image"),
        FieldPanel("hero_description"),
        FieldPanel("hero_button_text"),
        FieldPanel("hero_button_url"),
        FieldPanel("featured_description"),
        PageChooserPanel("featured_grid_item_1", GridItem),
        PageChooserPanel("featured_grid_item_2", GridItem),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            HERO_PANELS,
            heading="Hero Section (Optional)",
            classname="collapsible collapsed",
        ),
        InlinePanel(
            "grid_index_grid_item_relationship",
            label="grid_items",
            panels=None,
            min_num=1,
        ),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("hero_description"),
    ]

    class Meta:
        abstract = True

    def __str__(self):
        return "{0}".format(
            self.grid_items,
        )


class GridIndexPage(GridIndexPageAbstract, Page):
    """
    Concrete implementation of GridIndexPageAbstract.
    """

    class Meta:
        verbose_name = "Grid Index Page"
