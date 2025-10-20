
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
        
    
    