from lib.birthday import *

def test_add_birthday():
    birthday = Birthday()
    birthday.add_birthday("euan", "12/08/2025")
    assert birthday.birthday_dict == {"euan": "12/08/2025"}

def test_update_birthday():
    birthday = Birthday()
    birthday.add_birthday("euan", "12/08/2025")
    birthday.update_birthday("euan", "11/07/2025")

    assert birthday.birthday_dict ==  {"euan": "11/07/2025"}
    
def test_update_name():
    birthday = Birthday()
    birthday.add_birthday("euan", "12/08/2025")
    birthday.update_name("euan", "12/08/2025", "michael")

    assert birthday.birthday_dict == {"michael": "12/08/2025"}

def test_get_upcoming_birthdays():

    birthday = Birthday()
    birthday.add_birthday("euan", "10/11/2000")
    result = birthday.upcoming_birthday()

    assert result == {"euan": "10/11/2000"}

def test_get_upcoming_birthday_age():

    birthday = Birthday()
    birthday.add_birthday("euan", "22/10/2000")
    result = birthday.upcoming_birthday_age()

    assert result == {"euan": 25}
    