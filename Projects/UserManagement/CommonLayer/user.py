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