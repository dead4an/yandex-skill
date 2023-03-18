from skill_requests.Response import Response
from database.manage import DatabaseManager
from .skill_buttons import MAIN_MENU_BUTTONS, HELLO_BUTTONS
from .skill_texts import HELLO_TEXT, ABOUT_TEXT
from datetime import datetime as dt
import pytz

# state 1: выбор функции
# state 2: переключение на нужную функцию

USER_OPTIONS = {
    'name': 'user',
    'checkin-activities': None,
    'timezone': 3
}


class DialogHandler:
    """ Управляет диалогом """
    def __init__(self, user_id, command, session_state,
                 session_is_new, timezone):
        self.__user_id = user_id
        self.command = command
        self.session_state = session_state
        self.session_is_new = session_is_new
        self.user_exists = None
        self.timezone = timezone
        self.result = None

        self.check_user_is_new()

    def process(self):
        """ Обработка команды """
        if self.session_is_new:
            self.new_session()
            return

        if not self.user_exists:
            print('new')

        if self.session_state == 1: self.main_menu()
        elif self.process_command() == 2: self.process_command()

    def process_command(self):
        """ Обработка команды пользователя """
        # Команда не распознана
        if self.command == 'none':
            self.command_not_found()
            return

        match self.command:
            case 'about':
                text = ABOUT_TEXT
                buttons = MAIN_MENU_BUTTONS
                self.result = Response(text, buttons, session_state=2)

            case 'checkin':
                text = 'Отметка сделана!'
                buttons = MAIN_MENU_BUTTONS

                write_checkin(self.__user_id, self.timezone)
                self.result = Response(text, buttons, session_state=2)

            case 'statistic':
                checkins = read_checkins(self.__user_id)
                text = ''
                buttons = MAIN_MENU_BUTTONS
                for row in checkins[:10]:
                    text += f'Time: {row[0]} | Text: {row[1]}\n'

                self.result = Response(text, buttons, session_state=2)

    def command_not_found(self):
        """ Команда не найдена """
        text = 'Извините, я не знаю такой команды'
        buttons = MAIN_MENU_BUTTONS
        self.result = Response(text=text, buttons=buttons, session_state=2)

    def check_user_is_new(self):
        db = DatabaseManager('users.db')
        self.user_exists = db.check_user_exists(self.__user_id)
        db.insert_user(self.__user_id, options=USER_OPTIONS)

    def respond(self):
        return self.result.respond()

    # Функции диалога
    def new_session(self):
        """ Новая сессия в навыке """
        buttons = HELLO_BUTTONS['hello_new']
        text = HELLO_TEXT
        self.result = Response(text, buttons, session_state=1)

    def main_menu(self):
        """ Главаное меню навыка """
        text = "Что бы Вы хотели сделать?"
        buttons = MAIN_MENU_BUTTONS
        self.result = Response(text, buttons, session_state=2)


def write_checkin(user_id, timezone):
    """ Создаёт отметку в базе данных """
    tz = pytz.timezone(timezone)
    current_time = dt.now(tz)
    db = DatabaseManager('checkins.db')
    db.insert_checkin(user_id, current_time, 'works')


def read_checkins(user_id):
    """ Возвращает отметки пользователя """
    db = DatabaseManager('checkins.db')
    return db.select_checkins(user_id)
