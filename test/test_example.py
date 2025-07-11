import pytest

class Student():
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years

@pytest.fixture()
def default_employee():
    return Student('erfan', 'alishahi', 'physics', 4)


def test_person_initialization(default_employee):
    assert default_employee.first_name == 'erfan', 'first name should be erfan'
    assert default_employee.last_name == 'alishahi', 'last name should be alishahi'
    assert default_employee.major == 'physics'
    assert default_employee.years == 4