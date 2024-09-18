import pytest


@pytest.mark.django_db
def test_create_page(grid_index_page):
    """
    Tests creating a Gridder page.
    """
    assert grid_index_page.slug == "grid-index-page"
    assert grid_index_page.featured_description == "Featured description"
    assert grid_index_page.hero_button_text == "Hero button"
    assert grid_index_page.grid_items[0].title == "TEST Grid Item"
