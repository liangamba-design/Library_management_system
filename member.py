class Member:
    def __init__(self, member_id: str, name: str, email: str, phone: str):
        self.__member_id: str = member_id
        self.__name: str = name
        self.__email: str = email
        self.__phone: str = phone

    @property
    def member_id(self):
        return self.__member_id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email
    
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone