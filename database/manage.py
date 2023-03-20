import sqlite3 as sq

CREATE_TABLE_CHECKINS = "CREATE TABLE IF NOT EXISTS checkins (user_id, time, type, checkin_type)"
INSERT_CHECKIN = "INSERT INTO checkins VALUES (?,?,?,?)"
SELECT_CHECKINS = "SELECT time, checkin_type FROM checkins WHERE user_id=?"
SELECT_ALL_CHECKINS = "SELECT * FROM checkins"

CREATE_TABLE_ACTIVITIES = "CREATE TABLE IF NOT EXISTS activities (user_id, activity_id, time, activity_type)"
INSERT_ACTIVITY = "INSERT INTO activities VALUES (?,?,?)"
SELECT_ACTIVITIES = "SELECT time, activity_type FROM activities WHERE user_id=?"
DELETE_ACTIVITY = "DELETE FROM activities WHERE user_id=? AND activity_id=?"

CREATE_TABLE_USERS = "CREATE TABLE IF NOT EXISTS users (user_id, name, activities, timezone)"
INSERT_USER = "INSERT INTO users VALUES (?,?,?,?)"
USER_EXISTS = "SELECT 1 FROM users WHERE user_id=? LIMIT 1"


class DatabaseManager:
    def __init__(self, path_to_db):
        self.con: sq.Connection
        self.cur: sq.Cursor

        self.path_to_db = path_to_db
        self.con = None
        self.cur = None

    # Работа с отметками
    def insert_checkin(self, user_id, time, type, checkin_type):
        """ Загружает отметку в базу данных """
        try:
            self.setup_connection()
            self.cur.execute(CREATE_TABLE_CHECKINS)
            self.cur.execute(INSERT_CHECKIN, (user_id, time, type, checkin_type))
            self.con.commit()
        except Exception as _ex:
            print(f'Cannot insert checkin\n{_ex}')
        finally:
            self.close_connection()

    def select_checkins(self, user_id):
        """ Возвращает отметки пользователя """
        try:
            self.setup_connection()
            self.cur.execute(SELECT_CHECKINS, (user_id,))
            return self.cur.fetchall()
        except Exception as _ex:
            print(f'Cannot select checkins\n{_ex}')
        finally:
            self.close_connection()

    # Работа с пользователями
    def insert_user(self, user_id, options):
        try:
            self.setup_connection()
            self.cur.execute(CREATE_TABLE_USERS)

            name = options['name']
            activities = options['checkin-activities']
            timezone = options['timezone']

            self.cur.execute(INSERT_USER, (user_id, name, activities, timezone))
            self.con.commit()
        except Exception as _ex:
            print(f'Cannot insert user\n{_ex}')
        finally:
            self.close_connection()

    def check_user_exists(self, user_id):
        try:
            self.setup_connection()
            self.cur.execute(CREATE_TABLE_USERS)
            return self.cur.execute(USER_EXISTS, (user_id,)).fetchone()
        except Exception as _ex:
            print(f'Cannot select user (check)\n{_ex}')
        finally:
            self.close_connection()

    # Работа с соединением
    def setup_connection(self):
        try:
            self.con = sq.connect(self.path_to_db)
            self.cur = self.con.cursor()
        except Exception as _ex:
            self.close_connection()
            print(f'Cannot setup connection to database\n{_ex}')

    def close_connection(self):
        try:
            self.cur.close()
            self.con.close()
        except Exception as _ex:
            print(f'Cannot close connection\n{_ex}')
