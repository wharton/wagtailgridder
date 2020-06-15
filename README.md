# Wagtail Gridder

Wagtail Gridder is a Bootstrap 4 enabled layout for the Wagtail CMS. Grid Items are created within categories and displayed on a Grid Index Page. The JavaScript libraries Gridder and MixItUp are included.

# Requirements

* Django >= 2.2
* Wagtail >= 2.0
* Bootstrap >= 4

These installation instructions assume you are using Wagtail 2.0 or greater.

# Installation

*This installation assumes that you already have Django and Wagtail installed as part of your project.*

Wagtail Gridder can then be installed like most Django apps. First, install it into your `venv`:

    pip install wagtailgridder

Then add `wagtailgridder` to your list of `INSTALLED_APPS` in your Django settings file. You will also need to add `wagtail.contrib.modeladmin`, if you haven't already. Your final settings may look something like this:

```python
WAGTAIL_APPS = [
    'taggit',
    'modelcluster',
    'wagtail.core',
    'wagtail.admin',
    'wagtail.documents',
    'wagtail.snippets',
    'wagtail.users',
    'wagtail.images',
    'wagtail.embeds',
    'wagtail.search',
    'wagtail.sites',
]

WAGTAIL_CONTRIB_APPS = [
    'wagtailgridder',
    'wagtail.contrib.modeladmin',
]

INSTALLED_APPS = INSTALLED_APPS + WAGTAIL_APPS + WAGTAIL_CONTRIB_APPS
```

This Wagtail Gridder template extends `base.html`, with the hope that this allows inclusion or your site's top and bottom navigation without much effort. There is [an example base.html provided](https://github.com/wharton/wagtailgridder/blob/master/wagtailgridder/templates/base.html).

Then log into the Wagtail admin, and you should see a "Grid Layouts" section of the menu. The first thing you will want to do is add some "Grid Categories." After that, you can create "Grid Items" (the cards, pictured below) and put them together on a "Grid Index Page."

# Settings

    WAGTAILGRIDDER_CLEAR_CACHE = False

The default Wagtail Gridder template caches the grid display area to reduce the number of queries performed. Setting `WAGTAILGRIDDER_CLEAR_CACHE = True` in your Django settings will clear the **entire** Django cache after a page is edited. This approach is necessary, as Django does not currently support deletion from the cache by pattern. Setting this to `True` will clear your cache every time you save a Wagtail page. If anyone knows of a better solution that works for Django's supported cache systems, please let us know!

    WAGTAILGRIDDER_GRID_ITEM_PARENT_PAGE_TYPES = ["GridIndexPage"]

By default, GridItem pages may only be created as children of GridIndexPage pages. To
 allow GridItem pages under any parent, set
  `WAGTAILGRIDDER_GRID_ITEM_PARENT_PAGE_TYPES = None`. See the [Wagtail Documentation
  ](https://docs.wagtail.io/en/stable/reference/pages/model_reference.html#wagtail.core.models.Page)
  for more
# Screenshots

## Grid Index Page:

![Grid Index Page](https://raw.githubusercontent.com/wharton/wagtailgridder/master/img/grid_index_page.jpg)

## Grid Index Page, with Grid Item expanded:

![Grid Index Page, with Grid Item expanded](https://raw.githubusercontent.com/wharton/wagtailgridder/master/img/grid_index_page_expanded.jpg)

## Optional featured hero region:

![Optional featured hero region](https://raw.githubusercontent.com/wharton/wagtailgridder/master/img/featured_hero.jpg)

## Grid Item landing page:

![Grid Item landing page](https://raw.githubusercontent.com/wharton/wagtailgridder/master/img/grid_item.jpg)

## Editing a Grid Item:

![Editing a Grid Item](https://raw.githubusercontent.com/wharton/wagtailgridder/master/img/edit_grid_item.jpg)

## Editing a Grid Index Page:

![Editing a Grid Index Page](https://raw.githubusercontent.com/wharton/wagtailgridder/master/img/edit_grid_index_page.jpg)

# Release Notes

Release notes are [available on GitHub](https://github.com/wharton/wagtailgridder/releases).

# Contributors

* [Timothy Allen](https://github.com/FlipperPA)
* [Charles Rejonis](https://github.com/rejonis)
* [Noel Victor](https://github.com/noeldvictor)
