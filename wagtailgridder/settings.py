from django.conf import settings


def get_clear_cache():
    """
    Default to clearing the cache after each page edit.
    """

    return getattr(settings, "WAGTAILGRIDDER_CLEAR_CACHE", False)


def get_grid_item_parent_page_types():
    """
    Default parent page types for grid items.
    """

    return getattr(
        settings,
        "WAGTAILGRIDDER_GRID_ITEM_PARENT_PAGE_TYPES",
        ["GridIndexPage"]
    )

def get_grid_index_page_subpage_types():
    """
    Default subpage types for grid index pages.
    """

    return getattr(
        settings,
        "WAGTAILGRIDDER_GRID_INDEX_PAGE_SUBPAGE_TYPES",
        ["GridItem"]
    )
