from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register
)
from .models import (
    GridCategory, GridIndexPage
)


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
