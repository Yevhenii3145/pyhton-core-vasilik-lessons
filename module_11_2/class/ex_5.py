# Хранилище с паролем

class KeyStore:
    def __init__(self, name, password):
        self.__password = None
        self.__name = None
        self.__api_key = None
        self.name = name
        self.password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def password(self):
        return "No way to get password"

    @password.setter
    def password(self, new_password):
        if self.__password is None:
            self.__password = new_password
        elif self.is_validate():
            self.__password = new_password

    @property
    def api_key(self):
        if self.is_validate():
            return self.__api_key

    @api_key.setter
    def api_key(self, value):
        if self.is_validate():
            self.__api_key = value

    def is_validate(self):
        p = input("Password: ")
        if self.__password == p:
            print("OK")
            return True
        print("Wrong password")
        return False


k_store = KeyStore("Oksana", "123456")
print("Read password")
print(k_store.password)  # No way to get password
k_store.password = "567234"
print("Set secret value")
k_store.api_key = "Test"
print("Read secret value")
print(k_store.api_key)
