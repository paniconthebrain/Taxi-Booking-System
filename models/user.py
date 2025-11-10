from database.database_manager import DatabaseManager

class User:
    def __init__(self, name, username, password, contact, user_id=None):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.password = password
        self.contact = contact

    def save_to_db(self, role):
        db = DatabaseManager()
        db.connect()
        try:
            user_data = db.insert_user(self.name, self.username, self.password, self.contact, role)
            if user_data:
                self.user_id = user_data['user_id']
                print(f"{role.capitalize()} '{self.username}' registered successfully with ID {self.user_id}.")
            else:
                print(f"Registration failed for {role} '{self.username}'. Possibly username already exists.")
        except Exception as e:
            print("Error while saving user:", e)
        finally:
            db.close()


class Passenger(User):
    def __init__(self, name, username, password, contact, user_id=None):
        super().__init__(name, username, password, contact, user_id)

    def register(self):
        self.save_to_db('passenger')


class Driver(User):
    def __init__(self, name, username, password, contact, user_id=None):
        super().__init__(name, username, password, contact, user_id)

    def register(self):
        self.save_to_db('driver')


class Admin(User):
    def __init__(self, name, username, password, contact, user_id=None):
        super().__init__(name, username, password, contact, user_id)

    def register(self):
        self.save_to_db('admin')
