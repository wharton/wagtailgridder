from json import dumps as json_dumps

from django.contrib.contenttypes.models import ContentType

import pytest
from wagtail.models import Page
from wagtailgridder.models import GridIndexPage, GridItem, GridIndexGridItemRelationship


@pytest.fixture
def grid_index_page(db):
    """
    Create a root page in the same way Wagtail does in migrations. See:
    https://github.com/wagtail/wagtail/blob/main/wagtail/core/migrations/0002_initial_data.py#L12  # noqa

    Then create the test page.
    """
    page_content_type, created = ContentType.objects.get_or_create(
        model="page", app_label="wagtailcore"
    )

    root_page, created = Page.objects.get_or_create(
        title="Root",
        slug="root",
        content_type=page_content_type,
        path="0001",
        depth=1,
        numchild=1,
        url_path="/",
    )

    grid_index_page, created = GridIndexPage.objects.get_or_create(
        # Required Wagtail Page fields
        title="TEST Grid Index Page",
        slug="grid-index-page",
        content_type=page_content_type,
        path="000100010001",
        depth=3,
        numchild=1,
        url_path="/grid-index-page/",
        # Wagtail Grid Index Page fields
        featured_description="Featured description",
        hero_button_text="Hero button",
        hero_button_url="https://wagtail.org/",
        hero_description="Hero description",
    )

    grid_item, created = GridItem.objects.get_or_create(
        # Required Wagtail Page fields
        title="TEST Grid Item",
        slug="grid-item",
        content_type=page_content_type,
        path="0001000100010001",
        depth=4,
        numchild=0,
        url_path="/grid-index-page/grid-item",
        # Wagtail Grid Item fields
        buttons=json_dumps([
            {
                "type": "button_section",
                "value": {
                    "action_items": [
                        {
                            "type": "url_button",
                            "value": {
                                "label": "Wagtail",
                                "url": "https://wagtail.org",
                            },
                            "id": "25843f25-5ede-4a53-ae47-94fcd3f07f76",
                        }
                    ]
                },
                "id": "03abac3c-bded-43d6-9f87-352757733a0e",
            },
        ]),
        landing_page_text="Landing page text",
        summary_text="Summary text",
        description_text="Description text",
    )

    gi_relationship, created = GridIndexGridItemRelationship.objects.get_or_create(
        grid_relationship=grid_index_page,
        grid_item=grid_item,
    )

    return grid_index_page
