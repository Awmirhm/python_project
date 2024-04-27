import sqlite3
from CommonLayer.user import User
from CommonLayer.logs_class import Logs


class UserDataAccess:
    def __init__(self):
        self.data_base_name = "UserManagement.db"
        self.data_base_logs = "logs.db"

    # For Logs
    def logs(self, function_name, call_datatime, execution_time, username_clicker):
        with sqlite3.connect(self.data_base_logs) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO Logs (
                         function_name,
                         call_data_time,
                         execution_time,
                         username_clicker
                                 )
                VALUES           (
                         ?,
                         ?,
                         ?,
                         ?
                                 )""", [function_name, call_datatime, execution_time, username_clicker])
            connection.commit()

    def fetch_logs(self):
        logs = []
        with sqlite3.connect(self.data_base_logs) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT id,
                           function_name,
                           call_data_time,
                           execution_time,
                           username_clicker
                    FROM Logs
                    ORDER by execution_time DESC
                    """).fetchall()
            for item in data:
                log = Logs(item[0], item[1], item[2], item[3], item[4])
                logs.append(log)
            return logs

    def delete_log(self, log_id):
        with sqlite3.connect(self.data_base_logs) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                    DELETE FROM Logs
                    WHERE id = ?""", [log_id])
            connection.commit()

    #

    def get_user(self, username, password):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT id,
                           first_name,
                           last_name,
                           username,
                           email,
                           gender_id,
                           age,
                           country,
                           city,
                           active,
                           role_id
                    FROM User
                    WHERE  username = ?
                    AND    password = ?""", [username, password]).fetchone()

            if data:
                user = User(data[0], data[1], data[2], data[3], None, data[4], data[5], data[6], data[7], data[8],
                            data[9], data[10])
                return user
            else:
                return None

    def get_users(self, current_user_id):
        users = []
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT id,
                           first_name,
                           last_name,
                           username,
                           email,
                           gender_id,
                           age,
                           country,
                           city,
                           active,
                           role_id
                    FROM User
                    WHERE  id != ? """, [current_user_id]).fetchall()

            for item in data:
                user = User(item[0], item[1], item[2], item[3], None, item[4], item[5], item[6], item[7], item[8],
                            item[9], item[10])
                users.append(user)
            return users

    def update_status(self, active, username_user):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                    UPDATE User
                    SET active     = ?
                    WHERE username = ?""", [active, username_user])
            connection.commit()

    def update_role(self, role, username_user):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                    UPDATE  User
                    SET     role_id  = ?
                    WHERE   username = ?""", [role, username_user])
            connection.commit()

    def delete_user(self, username_user):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                    DELETE FROM User
                    WHERE  username = ?""", [username_user])
            connection.commit()

    def create_account(self, firstname, lastname, username, password, email, gender, age, country, city):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            INSERT INTO User (
                     first_name,
                     last_name,
                     username,
                     password,
                     email,
                     gender_id,
                     age,
                     country,
                     city,
                     active,
                     role_id
                 )
                 VALUES (
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     ?,
                     '{0}',
                     '{4}'
                            )""", [firstname, lastname, username, password, email, gender, age, country, city])
            connection.cursor()

    def return_all_username(self):
        usernames = []
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                SELECT id,
                       first_name,
                       last_name,
                       username,
                       email,
                       gender_id,
                       age,
                       country,
                       city,
                       active,
                       role_id
                FROM User
                            """).fetchall()
            for item in data:
                usernames.append(item[3])
            return usernames

    def edit(self, firstname, lastname, username, email, age, country, city, current_user_id):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                            UPDATE User
                            SET first_name = ?,
                                   last_name = ?,
                                   username = ?,
                                   email = ?,
                                   age   = ?,
                                   country = ?,
                                   city = ?
                            WHERE id = ?""",
                           [firstname, lastname, username, email, age, country, city, current_user_id])
            connection.commit()

    def user_information_for_profile(self, current_user_id):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT id,
                           first_name,
                           last_name,
                           username,
                           email,
                           gender_id,
                           age,
                           country,
                           city,
                           active,
                           role_id
                    FROM User
                    WHERE  id = ?""", [current_user_id]).fetchone()
            if data:
                user = User(data[0], data[1], data[2], data[3], None, data[4], data[5], data[6], data[7], data[8],
                            data[9], data[10])
                return user
            else:
                return None
