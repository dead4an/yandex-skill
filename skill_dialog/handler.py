from skill_requests.Response import Response
from database.manage import DatabaseManager
from .skill_buttons import SKILL_BUTTONS, MAIN_MENU_BUTTONS, HELP_BUTTONS, CARDS
from .skill_texts import TEXTS
from datetime import datetime as dt
import pytz
import random

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

        if self.command == 'none':
            self.command_not_found()
            return
        
        if self.session_state == 1:
            if self.command == 'yes':
                self.main_menu()
                return
            
            if self.command == 'no':
                text = 'Удачи!'
                self.result = Response(text=text, end_session=True)
                return
        
            if self.command == 'help':
                self.help()

            elif self.command == 'activities':
                    text = 'Отметка сделана!'
                    buttons = MAIN_MENU_BUTTONS
                    write_checkin(self.__user_id, self.timezone)
                    self.result = Response(text, buttons, session_state=1)

            elif self.command == 'statistic':
                    checkins = read_checkins(self.__user_id)
                    text = 'TEXT'
                    buttons = MAIN_MENU_BUTTONS
                    card = CARDS['card']
                    for row in checkins[:10]:
                        text += f'Time: {row[0]} | Text: {row[1]}\n'

                    self.result = Response(text, buttons, card, session_state=1)

        elif self.session_state == 2:
            if self.command == 'about_skill':
                self.about_skill()
            elif self.command == 'about_activities':
                self.about_activities()
            elif self.command == 'about_statistic':
                self.about_statistic()
            elif self.command in 'back' or 'back_to_menu':
                self.main_menu()

    def command_not_found(self):
        """ Команда не найдена """
        text = 'Извините, я не знаю такой команды'
        buttons = MAIN_MENU_BUTTONS
        self.result = Response(text=text, buttons=buttons, session_state=1)

    def check_user_is_new(self):
        """ Проверка нового пользователя """
        db = DatabaseManager('users.db')
        self.user_exists = db.check_user_exists(self.__user_id)
        if not self.user_exists: 
            db.insert_user(self.__user_id, options=USER_OPTIONS)

    def respond(self):
        return self.result.respond()

    # Функции диалога
    def new_session(self):
        """ Новая сессия в навыке """
        text = None
        buttons = None

        if self.user_exists:
            text = random.choice(TEXTS['hello_std'])
            buttons = MAIN_MENU_BUTTONS

        else:
            text = TEXTS['hello_new']
            buttons = [SKILL_BUTTONS['hello_new']]

        self.result = Response(text, buttons, session_state=1)

    def main_menu(self):
        """ Главаное меню навыка """
        text = "Что бы Вы хотели сделать?"
        buttons = MAIN_MENU_BUTTONS
        self.result = Response(text, buttons, session_state=1)

    def help(self):
        """ Помощь пользователю """
        text = TEXTS['help']
        buttons = HELP_BUTTONS
        self.result = Response(text, buttons, session_state=2)

    def about_skill(self):
        text = TEXTS['about_skill']
        buttons = HELP_BUTTONS
        self.result = Response(text, buttons, session_state=2)

    def about_activities(self):
        text = TEXTS['about_activities']
        buttons = HELP_BUTTONS
        self.result = Response(text, buttons, session_state=2)

    def about_statistic(self):
        text = TEXTS['about_statistic']
        buttons = HELP_BUTTONS
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
