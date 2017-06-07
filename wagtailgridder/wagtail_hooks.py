from django.core.cache import cache

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register
)
from wagtail.wagtailcore import hooks

from .models import (
    GridCategory, GridIndexPage
)
from .settings import get_clear_cache


class GridCategoryAdmin(ModelAdmin):
    model = GridCategory
    menu_label = 'Grid Categories'
    menu_icon = 'fa-folder-open'
    add_to_settings_menu = False
    list_display = ('name',)
    search_fields = ('name',)


class GridIndexPageAdmin(ModelAdmin):
    model = GridIndexPage
    menu_icon = 'doc-full-inverse'
    list_display = ('title',)
    search_fields = ('title',)


class GridAdminGroup(ModelAdminGroup):
    menu_label = 'Grid Layouts'
    menu_icon = 'fa-th'  # change as required
    menu_order = 400  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (GridCategoryAdmin, GridIndexPageAdmin)


modeladmin_register(GridAdminGroup)


@hooks.register('after_edit_page')
def clear_page_cache(request, page):
    """
    This will clear Django's entire cache after a page edit. It is ugly,
    but Django's cache mechanism doesn't currently support a way to easily
    depending on the value of is_staff() and (if present) is_faculty.
    """

    if get_clear_cache():
        cache.clear()
