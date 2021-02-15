# Wagtail Gridder

Wagtail Gridder is a Bootstrap 4 enabled layout for the Wagtail CMS. Grid Items are created within categories and displayed on a Grid Index Page. The JavaScript libraries Gridder and MixItUp are included.

# Requirements

* Django >= 2.2
* Wagtail >= 2.0
* Bootstrap >= 4

# Installation

*This installation assumes that you already have Django 2.2+ and Wagtail 2.0+ installed as part of your project.*

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

This Wagtail Gridder template extends `base.html`, with the hope that this allows inclusion or your site's top and bottom navigation without much effort. There is [an example base.html provided](https://github.com/wharton/wagtailgridder/blob/main/wagtailgridder/templates/base.html).

Then log into the Wagtail admin, and you should see a "Grid Layouts" section of the menu. The first thing you will want to do is add some "Grid Categories." After that, you can create "Grid Items" (the cards, pictured below) and put them together on a "Grid Index Page."

# Settings

    WAGTAILGRIDDER_CLEAR_CACHE = False

The default Wagtail Gridder template caches the grid display area to reduce the number of queries performed. Setting `WAGTAILGRIDDER_CLEAR_CACHE = True` in your Django settings will clear the **entire** Django cache after a page is edited. This approach is necessary, as Django does not currently support deletion from the cache by pattern. Setting this to `True` will clear your cache every time you save a Wagtail page. If anyone knows of a better solution that works for Django's supported cache systems, please let us know!

    WAGTAILGRIDDER_GRID_ITEM_PARENT_PAGE_TYPES = ["GridIndexPage"]

By default, GridItem pages may only be created as children of GridIndexPage pages. To
 allow GridItem pages under any parent, set
  `WAGTAILGRIDDER_GRID_ITEM_PARENT_PAGE_TYPES = None`. See the [Wagtail Documentation
  ](https://docs.wagtail.io/en/stable/reference/pages/model_reference.html#wagtail.core.models.Page.parent_page_types)
  for more

    WAGTAILGRIDDER_GRID_INDEX_PAGE_SUBPAGE_TYPES = ["GridItem"]

By default, GridIndexPage pages may only have GridItem pages as children. To allow GridIndexPage pages to have other child types, set `WAGTAILGRIDDER_GRID_INDEX_PAGE_SUBPAGE_TYPES = None`. See the [Wagtail Documentation](https://docs.wagtail.io/en/stable/reference/pages/model_reference.html#wagtail.core.models.Page.subpage_types) for more details.

`GridIndexPage` is inherited from an abstract model, [GridIndexPageAbstract](https://github.com/wharton/wagtailgridder/blob/a559ad39ec9f3bc1291080eb7e7cf5a60ffb5b38/wagtailgridder/models.py#L175), which you may wish to customize.

# Screenshots

## Grid Index Page:

![Grid Index Page](https://raw.githubusercontent.com/wharton/wagtailgridder/main/img/grid_index_page.jpg)

## Grid Index Page, with Grid Item expanded:

![Grid Index Page, with Grid Item expanded](https://raw.githubusercontent.com/wharton/wagtailgridder/main/img/grid_index_page_expanded.jpg)

## Optional featured hero region:

![Optional featured hero region](https://raw.githubusercontent.com/wharton/wagtailgridder/main/img/featured_hero.jpg)

## Grid Item landing page:

![Grid Item landing page](https://raw.githubusercontent.com/wharton/wagtailgridder/main/img/grid_item.jpg)

## Editing a Grid Item:

![Editing a Grid Item](https://raw.githubusercontent.com/wharton/wagtailgridder/main/img/edit_grid_item.jpg)

## Editing a Grid Index Page:

![Editing a Grid Index Page](https://raw.githubusercontent.com/wharton/wagtailgridder/main/img/edit_grid_index_page.jpg)

## Maintainer

* [Timothy Allen](https://github.com/FlipperPA) at [The Wharton School](https://github.com/wharton)

This package is maintained by the staff of [Wharton Research Data Services](https://wrds.wharton.upenn.edu/). We are thrilled that [The Wharton School](https://www.wharton.upenn.edu/) allows us a certain amount of time to contribute to open-source projects. We add features as they are necessary for our projects, and try to keep up with Issues and Pull Requests as best we can. Due to constraints of time (our full time jobs!), Feature Requests without a Pull Request may not be implemented, but we are always open to new ideas and grateful for contributions and our package users.

## Contributors (Thank You!)

* [Charles Rejonis](https://github.com/rejonis)
* [Noel Victor](https://github.com/noeldvictor)
* [Ryan Sullivan](https://github.com/tgs258)
