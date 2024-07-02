import pytest
from products import Product

def test_create_normal_product():
    product = Product("MacBook Air M2", 1450, 100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active()

def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", 1450, 100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", -10, 100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", 1450, -5)

def test_product_reaches_zero_quantity_becomes_inactive():
    product = Product("MacBook Air M2", 1450, 1)
    product.buy(1)
    assert product.quantity == 0
    assert not product.is_active()

def test_product_purchase_modifies_quantity_and_returns_correct_output():
    product = Product("MacBook Air M2", 1450, 10)
    total_price = product.buy(2)
    assert total_price == 2900  
    assert product.quantity == 8

def test_buying_larger_quantity_than_exists_raises_exception():
    product = Product("MacBook Air M2", 1450, 10)
    with pytest.raises(ValueError):
        product.buy(20)

if __name__ == "__main__":
    pytest.main()
