import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def api_client():
    """Фикстура для клиента API"""
    return APIClient()


@pytest.fixture
def product_factory():
    """Фабрика для курсов"""
    def factory(**kwargs):
        return baker.make('Product', **kwargs)
    return factory
