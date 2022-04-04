from django.core.cache import cache
from django.urls import reverse
from django.utils.translation import gettext as _
from wagtail.contrib.modeladmin.helpers import PageButtonHelper

from wagtail.core import hooks

from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from .models import GridCategory, GridIndexPage, GridIndexPageAbstract, GridItem
from .settings import get_clear_cache


class PageButtonHelperWithAddChild(PageButtonHelper):
    def create_child_button(self, pk, classnames_add=None, classnames_exclude=None):
        if classnames_add is None:
            classnames_add = []
        if classnames_exclude is None:
            classnames_exclude = []
        classnames = self.edit_button_classnames + classnames_add
        cn = self.finalise_classname(classnames, classnames_exclude)
        return {
            "url": reverse("wagtailadmin_pages:add_subpage", args=[pk]),
            "label": _("Add child page"),
            "classname": cn,
            "title": _("Add a child page to %s") % self.verbose_name,
        }

    def get_buttons_for_obj(
        self, obj, exclude=None, classnames_add=None, classnames_exclude=None
    ):
        btns = super().get_buttons_for_obj(
            obj, exclude, classnames_add, classnames_exclude
        )
        if classnames_add is None:
            classnames_add = []
        if classnames_exclude is None:
            classnames_exclude = []
        pk = getattr(obj, self.opts.pk.attname)
        btns.append(self.create_child_button(pk, classnames_add, classnames_exclude))

        return btns


class GridCategoryAdmin(ModelAdmin):
    model = GridCategory
    menu_label = "Grid Categories"
    menu_icon = "fa-folder-open"
    add_to_settings_menu = False
    list_display = ("name",)
    search_fields = ("name",)


class GridIndexPageAdmin(ModelAdmin):
    model = GridIndexPage
    menu_icon = "doc-full-inverse"
    list_display = ("title",)
    search_fields = ("title",)
    button_helper_class = PageButtonHelperWithAddChild


class GridAdminGroup(ModelAdminGroup):
    menu_label = "Grid Layouts"
    menu_icon = "fa-th"  # change as required
    menu_order = 400  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (GridCategoryAdmin, GridIndexPageAdmin)


modeladmin_register(GridAdminGroup)


@hooks.register("after_edit_page")
def clear_page_cache(request, page):
    """
    This will clear Django's entire cache after a page edit. It is ugly, but Django's
    cache mechanism doesn't currently support a way to easily clear based on template
    fragments specifics.
    """

    if get_clear_cache() and isinstance(page, (GridItem, GridIndexPageAbstract)):
        cache.clear()
