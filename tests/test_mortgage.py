import mortgage
import decimal

def test_pound():
    assert mortgage.pound(1.314159) == decimal.Decimal('1.31')
