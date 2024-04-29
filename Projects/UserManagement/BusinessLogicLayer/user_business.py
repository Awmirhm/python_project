from DataAccessLayer.user_data_access import UserDataAccess


class UserBusiness:
    def __init__(self):
        self.user_data_access = UserDataAccess()

    def login(self, username, password):
        if len(username) < 3 or len(password) < 3:
            return [None, "Invalid Request"]
        else:
            user = self.user_data_access.get_user(username, password)

        if user:
            if user.active == 0:
                return [None, "Your Account Deactivate"]
            else:
                return [user, None]
        else:
            return [None, "Invalid Username or Password"]

    def get_users(self, current_user, sort):
        if current_user.role_id != 1 and current_user.role_id != 2 and current_user.role_id != 3:
            return [None, "Invalid Access"]
        if current_user.active == 0:
            return [None, "Your Account Deactivate"]
        else:
            users = self.user_data_access.get_users(current_user.id)
            if sort == "Name":
                sort_by_name = sorted(users, key=lambda name: name.firstname)
                return [sort_by_name, None]
            if sort == "Gender":
                sort_by_gender = sorted(users, key=lambda gender: gender.gender_id)
                return [sort_by_gender, None]
            if sort == "Age":
                sort_by_age = sorted(users, key=lambda age: age.age)
                return [sort_by_age, None]
            if sort == "Role":
                sort_bu_role = sorted(users, key=lambda role: role.role_id)
                return [sort_bu_role, None]
            return [users, None]

    def update_to_active(self, current_user, username_user):
        if current_user.role_id != 1 and current_user.role_id != 2 and current_user.role_id != 3:
            return "Invalid Access"
        if current_user.active == 0:
            return "Your Account Deactivate"
        else:
            self.user_data_access.update_status(1, username_user)
            return None

    def update_to_deactivate(self, current_user, username_user):
        if current_user.role_id != 1 and current_user.role_id != 2 and current_user.role_id != 3:
            return "Invalid Access"
        if current_user.active == 0:
            return "Your Account Deactivate"
        else:
            self.user_data_access.update_status(0, username_user)
            return None

    def update_to_super_admin(self, current_user, username_user):
        if current_user.role_id != 1:
            return "Invalid Access"
        if current_user.active == 0:
            return "Your Account Deactivate"
        else:
            self.user_data_access.update_role(2, username_user)
            return None

    def update_to_admin(self, current_user, username_user):
        if current_user.role_id != 1 and current_user.role_id != 2:
            return "Invalid Access"
        if current_user.active == 0:
            return "Your Account Deactivate"
        else:
            self.user_data_access.update_role(3, username_user)
            return None

    def update_to_default_user(self, current_user, username_user):
        if current_user.role_id != 1 and current_user.role_id != 2:
            return "Invalid Access"
        if current_user.active == 0:
            return "Your Account Deactivate"
        else:
            self.user_data_access.update_role(4, username_user)
            return None

    def delete_user(self, current_user, username_user):
        if current_user.role_id != 1:
            return "Invalid Access"
        if current_user.active == 0:
            return "Your Account Deactivate"
        else:
            self.user_data_access.delete_user(username_user)
            return None

    def signin(self, firstname, lastname, username, password, repeat_password, email, age, gender, country, city):
        usernames = self.user_data_access.return_all_username()

        if len(firstname) < 3 or len(lastname) < 3 or len(username) < 3 or len(password) < 3 or len(email) < 8 or len(
                age) < 1 or len(country) < 3 or len(city) < 3:
            return [None, "Fill in the blank fields"]

        if isinstance(firstname, int):
            return [None, "Invalid First Name"]

        if not isinstance(lastname, str):
            return [None, "Invalid Last Name "]

        if gender == "0":
            return [None, "Please specify your gender"]

        if password == repeat_password:
            for username_all_users in usernames:
                if username == username_all_users:
                    return [None, "Duplicate username"]

            self.user_data_access.create_account(firstname, lastname, username, password, email, gender, age,
                                                 country, city)
            return (
                "Your account has been successfully created. Please wait for your account to be activated by the admin",
                None)
        else:
            return [None, "Invalid Password"]

    def edit_information(self, current_user, firstname, lastname, username, email, age, country, city):
        usernames = self.user_data_access.return_all_username()

        if current_user.active == 0:
            return [None, "Your Account Deactivate"]
        if len(firstname) < 3 or len(lastname) < 3 or len(username) < 3 or len(email) < 3 or len(age) < 1 or len(
                country) < 3 or len(city) < 3:
            return [None, "Fill in the blank fields"]
        else:
            for all_usernames in usernames:
                if username == all_usernames:
                    return [None, "Duplicate username"]

            self.user_data_access.edit(firstname=firstname, lastname=lastname, username=username, email=email, age=age,
                                       country=country, city=city, current_user_id=current_user.id)
            return ["Your Data Changed", None]

    def profile(self, current_user):
        if current_user.active == 0:
            return [None, "Your Account Deactivate"]
        else:
            user = self.user_data_access.user_information_for_profile(current_user.id)
            return [user, None]

    def get_logs(self, current_user):
        if current_user.role_id != 1:
            return [None, "Invalid Access"]
        if current_user.active == 0:
            return [None, "Your Account Deactivate"]
        else:
            logs = self.user_data_access.fetch_logs()
            return [logs, None]

    def delete_for_log(self, current_user, log_id):
        if current_user.role_id != 1:
            return "Invalid Access"
        if current_user.active == 0:
            return "Your Account Deactivate"
        else:
            self.user_data_access.delete_log(log_id)
            return None
