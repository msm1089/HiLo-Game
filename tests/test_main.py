import program


def test_secret_number_in_range():
    secret_number = program.secret_number
    print("The secret number is {}.".format(secret_number))
    assert 1 <= secret_number & secret_number <= 100
