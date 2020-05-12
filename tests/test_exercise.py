import pytest
from src import product

def test_exercise(capsys):
    sausages = product.Product("sausage",1.2,14)
    sausages.print_product()

    out, err = capsys.readouterr()
    assert out == "sausage, price 1.2, 14 pcs\n"
