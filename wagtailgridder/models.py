from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils import timezone
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page, Orderable
from wagtail.search import index

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


class GridItemAbstract(models.Model):
    """
    The fields needed to properly display a grid item.
    The template will omit any fields not included automagically.
    """

    parent_page_types = get_grid_item_parent_page_types()

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
    buttons = StreamField(ButtonBlock(), null=True, use_json_field=True)
    tags = ClusterTaggableManager(through=GridItemTag, blank=True)
    categories = ParentalManyToManyField("GridCategory", blank=True)
    modified = models.DateTimeField("Page Modified", null=True)

    search_fields = Page.search_fields + [
        index.SearchField("summary_text"),
        index.SearchField("description_text"),
        index.SearchField("landing_page_text"),
    ]

    CARD_PANELS = [
        FieldPanel("summary_image"),
        FieldPanel("summary_text"),
    ]

    DETAIL_PANELS = [
        FieldPanel("description_image"),
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
        FieldPanel(
            "buttons",
        ),
        MultiFieldPanel(
            META_PANELS,
            heading="Metadata",
            classname="collapsible",
        ),
    ]

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.modified = timezone.now()
        super().save(*args, **kwargs)


class GridItem(GridItemAbstract, Page):
    """
    Concrete implementation of GridItemAbstract.
    """

    class Meta:
        verbose_name = "Grid Item"


class GridIndexGridItemRelationship(Orderable, models.Model):
    """
    Allows the content creator to associate Grid Items on a Grid Index Page.
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
    panels = [FieldPanel("grid_item")]


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
        help_text=(
            "The background image for the hero section. This triggers the section to "
            "be displayed if an image is selected."
        ),
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
        help_text=(
            "Text for the call-to-action button beneath the text and logo over the "
            "background image."
        ),
    )

    hero_button_url = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text=(
            "URL for the call-to-action button beneath the text and logo over the "
            "background image."
        ),
    )

    featured_description = RichTextField(
        null=True,
        blank=True,
        help_text=(
            "Text to be displayed below the hero image next to the featured items."
        ),
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

    def get_grid_items(self, request=None):
        """
        Returns the grid items associated with this page. This method may be overridden
        to provide custom processing of the grid items, particularly in context of the
        request.
        :param request: The request object, if available.
        :return: A list of grid items.
        """
        grid_items = [n.grid_item for n in self.grid_index_grid_item_relationship.all()]
        return grid_items

    @property
    def grid_items(self):
        """
        A convenience property to get the grid items associated with this page
        in the absence of a request object.
        :return: A list of grid items.
        """
        return self.get_grid_items()

    def get_categories(self, request=None):
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

    @property
    def categories(self):
        return self.get_categories()

    HERO_PANELS = [
        FieldPanel("hero_background_image"),
        FieldPanel("hero_logo_image"),
        FieldPanel("hero_description"),
        FieldPanel("hero_button_text"),
        FieldPanel("hero_button_url"),
        FieldPanel("featured_description"),
        FieldPanel("featured_grid_item_1"),
        FieldPanel("featured_grid_item_2"),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            HERO_PANELS,
            heading="Hero Section (Optional)",
            classname="collapsible collapsed",
        ),
        InlinePanel(
            "grid_index_grid_item_relationship",
            label="Grid Items",
            panels=None,
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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # Add grid_items to the context
        context["grid_items"] = self.get_grid_items(request)
        context["categories"] = self.get_categories(request)

        return context

    class Meta:
        verbose_name = "Grid Index Page"
