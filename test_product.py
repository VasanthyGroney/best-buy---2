import pytest
from products import Product

def test_create_normal_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100

def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)  # Empty name
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)  # Negative price

def test_product_becomes_inactive_when_quantity_zero():
    product = Product("MacBook Air M2", price=1450, quantity=0)
    assert not product.is_active()

def test_product_purchase_modifies_quantity_and_returns_correct_output():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(5)
    assert total_price == 1450 * 5
    assert product.quantity == 95

def test_purchase_larger_quantity_than_exists():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        product.buy(150)
