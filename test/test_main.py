from src.program import get_secret_number


def test_secret_number_in_range():
    secret_number = get_secret_number()
    assert 1 <= secret_number <= 100
