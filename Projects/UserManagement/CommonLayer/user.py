class User:
    def __init__(self, id, firstname, lastname, username, password, email, gender_id, age, country, city, active,
                 role_id):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email
        self.gender_id = gender_id
        self.age = age
        self.country = country
        self.city = city
        self.active = active
        self.role_id = role_id

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError(f"Invalid Value : {value}")
        self._firstname = value
