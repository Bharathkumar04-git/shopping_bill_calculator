from app import calculate_total

def test_calculate_total():
    assert calculate_total(10.5, 2) == 21.0
    assert calculate_total(0, 5) == 0.0
