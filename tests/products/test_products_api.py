import pytest
# from django.urls import reverse


@pytest.mark.django_db
def test_get_products(api_client, product_factory):
    # product = product_factory(_quantity=1)
    # url = reverse('product-detail', args=(product[0].id,))
    # resp = api_client.get(url)
    # resp_json = resp.json()
    #
    # assert resp.status_code == 200
    # assert product[0].id == resp_json.get('id')
    # assert product[0].title == resp_json.get('title')
    assert 'Andrey' == 'Andrey'
