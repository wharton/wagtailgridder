from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils import timezone

from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from .blocks import ButtonBlock


class GridItemTag(TaggedItemBase):
    """
    Object to hold existing tags for Grid Items.
    """

    content_object = ParentalKey('GridItem', related_name='tagged_items')


class GridCategory(models.Model):
    """
    Categories which a grid item can belong to. A grid item can belong to
    many categories. Categories can be selected from the top of the grid
    index page.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'grid categories'


class GridItem(Page):
    """
    The fields needed to properly display a grid item.
    The template will omit any fields not included automagically.
    """

    class Meta:
        verbose_name = "Grid Item"

    summary_text = RichTextField(
        'Summary',
        default='',
        help_text='The summary will appear in the item "card" view.',
    )
    description_text = RichTextField(
        'Full Description',
        default='',
        help_text='The description will appear when the grid item is clicked and expanded.',
    )
    landing_page_text = RichTextField(
        'Landing Page Text',
        default='',
        help_text='This is the text which will appear on the grid item\'s landing page.',
    )
    tags = ClusterTaggableManager(through=GridItemTag, blank=True)
    categories = ParentalManyToManyField('GridCategory', blank=True)
    modified = models.DateTimeField('Page Modified', null=True)
    summary_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    description_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    buttons = StreamField(ButtonBlock(), null=True)

    search_fields = Page.search_fields + [
        index.SearchField('summary_text'),
        index.SearchField('description_text'),
        index.SearchField('landing_page_text'),
    ]

    CARD_PANELS = [
        ImageChooserPanel('summary_image'),
        FieldPanel('summary_text'),
    ]

    DETAIL_PANELS = [
        ImageChooserPanel('description_image'),
        FieldPanel('description_text'),
        FieldPanel('landing_page_text'),
    ]

    META_PANELS = [
        FieldPanel('tags'),
        FieldPanel('categories', widget=CheckboxSelectMultiple),
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
            'buttons',
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
    GridRelationship = ParentalKey(
        'GridIndexPage',
        related_name='grid_index_grid_item_relationship'
    )
    grid_item = models.ForeignKey(
        'GridItem',
        related_name="+",
        help_text='Add a grid item to the page',
        verbose_name='Grid Items'
    )
    panels = [
        PageChooserPanel('grid_item')
    ]


class GridIndexPage(Page):
    """
    Index page for Grid Items.
    This links the grid items to the categories and provides a page to display them on.
    """

    @property
    def grid_items(self):
        grid_items = [
            n.grid_item for n in self.grid_index_grid_item_relationship.all()
        ]
        return grid_items

    @property
    def categories(self):
        categories = GridCategory.objects.all()
        return categories

    content_panels = Page.content_panels + [
        InlinePanel('grid_index_grid_item_relationship', label="grid_items", panels=None, min_num=1),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('grid_index_grid_item_relationship'),
    ]

    # Don't allow child pages to be added
    subpage_types = [
    ]

    class Meta:
        verbose_name = "Grid Index Page"

    def __str__(self):
        return '{0}'.format(
            self.grid_items,
        )
