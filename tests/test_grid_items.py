import pytest


@pytest.mark.django_db
def test_create_page(grid_index_page):
    """
    Tests creating a Gridder page.
    """
    assert False
    print(grid_index_page.render())
