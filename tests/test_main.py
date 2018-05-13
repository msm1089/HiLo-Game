import program


def test_secret_number_in_range():
    secret_number = program.get_secret_number()
    assert 1 <= secret_number <= 100
