import sys
import os
import pytest

# ensure project root is on sys.path so `from app import ...` works during pytest runs
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, products

@pytest.fixture
def client():
    with app.test_client() as c:
        yield c


def test_index_status(client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_index_contains_brand(client):
    resp = client.get('/')
    html = resp.get_data(as_text=True)
    assert 'Velora' in html
    assert 'Upgrade your everyday' in html


def test_products_render_count(client):
    resp = client.get('/')
    html = resp.get_data(as_text=True)
    # count only the product cards rendered by the loop (article elements)
    assert html.count('<article class="product-card">') == len(products)


def test_theme_toggle_present(client):
    resp = client.get('/')
    html = resp.get_data(as_text=True)
    assert 'id="theme-toggle"' in html
    assert 'theme.js' in html
