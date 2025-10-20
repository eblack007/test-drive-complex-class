from datetime import datetime

class Birthday():
    
    def __init__(self):
        self.birthday_dict = {}

    def add_birthday(self, name, dob):

        entry = {name: dob}
        self.birthday_dict.update(entry)

    def update_birthday(self, name, dob):

        if (name) in self.birthday_dict:
            self.birthday_dict[name] = dob
        else:
            return "Person does not exist!"
        
    def update_name(self, name, dob, newname):

        if (name) in self.birthday_dict:
            self.birthday_dict[newname] = self.birthday_dict[name]
            del self.birthday_dict[name]
        else:
            return "Person does not exist!"
        
    
    def upcoming_birthday(self):

        upcoming_bday = {}
        date_format = '%d/%m/%Y'
        today = datetime.today()

        for name, dob in self.birthday_dict.items():
            dob_formatted = datetime.strptime(dob, date_format)
            dob_formatted = dob_formatted.replace(year=today.year)

            dob_diff = today - dob_formatted

            if dob_diff.days <= 30:
                upcoming_bday.update({name: dob})

        return upcoming_bday
    
    def upcoming_birthday_age(self):

        upcoming_bday = {}
        date_format = '%d/%m/%Y'
        today = datetime.today()

        for name, dob in self.birthday_dict.items():
            dob_formatted = datetime.strptime(dob, date_format)

            dob_diff = today - dob_formatted
            age = dob_diff.days/365
            age = int(age)

            upcoming_bday.update({name: age})
            
        return upcoming_bday

        


        