# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem 

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

# Real

class Birthdays():

    def __init__(self):
        #Paramter
        #list of birthdays: empty dictionary
        # Arannged {[name: xx, birthday:  ], }

        # Returns n/a

        # side effects n/a

        pass

    def add_birthday(self, name, dob):
        # paeramter
        # string : name
        # date : birthday
        
        # return n/a

        # side effect save new entry to the self object
        pass

    def update_birthday(self, name, dob):
        # paeramter
        # string : name
        # string : birthday
        
        # return n/a

        # side effect updates existing birthday entry to the self object
        pass

    def update_name(self, name, dob):
        # paeramter
        # string : name
        # string : birthday
        
        # return n/a

        # side effect updates existing name entry to the self object
        pass

    def upcoming_birthday(self):
        # parametrs n/a

        # return
        # list of names whose birthdays are soon

        # side effects
        # n/a
        pass

    def upcoming_birthday_age(self):
        # paramters
        # upcoming_birthday_reminder

        # return
        # list: name sand ages of their upcomingf b-day

        # side effects
        # n/a
        pass




# EXAMPLE

class Reminder:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def remind_me_to(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def remind(self):
        # Returns:
        #   A string reminding the user to do the task
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python


# Real 
"""Given a name and a date of birth
a user is added to the dictionary
"""

birthday = Birthday()
birthday.add_birthday("euan", "12/08/2025")

assert self.birthdayDict == {"euan": "12/08/2025"}

"""Given a name and a date of birth
a date of birth is updated to the dictionary
"""

birthday = Birthday()
birthday.add_birthday("euan", "12/08/2025")
birthday.upade_birthday("euan", "11/07/2025")

assert self.birthdayDict == {"euan": "11/07/2025"}

"""Given a name and a date of birth
a name is updated to the dictionary
"""

birthday = Birthday()
birthday.add_birthday("euan", "12/08/2025")
birthday.update_name("miuchael", "12/08/2025")

assert self.birthdayDict == {"michael": "12/08/2025"}

"""Given a request a list of upcoming
birthdays is produced
"""

birthday = Birthday()
birthday.add_birthday("euan", "10/11/2025")
result = birthday.upcoming_birthday()

assert result = [
    {"euan":
    "10/11/2025"
    }
]


"""Given a request a list of upcoming birthday ages
is produced
"""
birthday = Birthday()
birthday.add_birthday("euan", "21/10/2000")
list_bday = birthday.upcoming_birthday()
upcoming_bday = upcoming_bday_age(list_bday)


assert upcoming_bdy = [
    {"euan":
    "25"
    }
]

# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
