import datetime


class Person:
    number_of_Person_instances = 0

    def __init__(self, firstname, lastname, dob, fav_color):
        self._firstname = firstname
        self._lastname = lastname
        self.__dob = dob
        self._fav_color = fav_color
        self.__person = True
        Person.number_of_Person_instances += 1

    def __str__(self):
        return f"{self.firstname} {self.lastname} is an instance of a class Person."

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, new_firstname):
        self._firstname = new_firstname

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, new_lastname):
        self._lastname = new_lastname

    @property
    def dob(self):
        return self.__dob

    # no setter for date of birth - it's semi private - as we decided we don't want users to change it

    @property
    def fav_color(self):
        return self._fav_color

    @fav_color.setter
    def fav_color(self, new_address):
        self._fav_color = new_address

    def calculate_age(self):
        age = datetime.date.today().year - self.dob.year - ((datetime.date.today().month, datetime.date.today().day) <
                                                            (self.dob.month, self.dob.day))
        return age

    def birthday(self):
        birthday = self.dob.strftime("%d") + " " + self.dob.strftime("%B")
        return birthday

    def is_person(self):
        return self.__person

    def walk(self):
        return f"{self.firstname} is walking"

    def walk_to(self, location):
        return f"{self.firstname} is walking to {location}"

    def talk(self):
        return f"{self.firstname} is talking"

    def laugh(self):
        return f"{self.firstname} is laughing"

    def information(self):
        information = self.firstname + " is an amazing human. " + "His/Her favourite colour is " + self.fav_color + \
                      ". Every year they celebrate their birthday on " + self.birthday() + "."
        return information

    @classmethod
    def get_number_of_person_instances(cls) -> int:
        return cls.number_of_Person_instances
