from skill_requests.Response import Response
from database.manage import DatabaseManager
from .skill_buttons import SKILL_BUTTONS, MAIN_MENU_BUTTONS, HELP_BUTTONS, CARDS
from .skill_texts import TEXTS
import datetime
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
        self.checkins_list = None
        self.activities_list = None
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
                self.activities()

            elif self.command == 'statistic':
                    self.get_checkins()
                    text = ''
                    buttons = MAIN_MENU_BUTTONS
                    for row in self.checkins[:10]:
                        text += f'Time: {row[0]} | Text: {row[1]}\n'

                    self.result = Response(text, buttons, session_state=1)

        elif self.session_state == 2:
            self.get_checkins()
            text = ''
            buttons = MAIN_MENU_BUTTONS
            if self.checkins and len(self.checkins) % 2 == 1:
                last_checkin_time = self.checkins[-1][0]
                last_checkin_time = self.get_time(last_checkin_time)
                activity_duration = self.get_time(return_timestamp=True) - last_checkin_time
                print(activity_duration)
                if self.command == 'activity_work':
                    self.add_checkin('stop', 'work')
                    text = 'Активность "Работа" была завершена!'
                elif self.command == 'activity_homework':
                    self.add_checkin('stop', 'homework')
                    text = 'Активность "Домашние Дела" была завершена!'
                elif self.command == 'activity_hobby':
                    self.add_checkin('stop', 'hobby')
                    text = 'Активность "Хобби" была завершена!'
                elif self.command == 'activity_sport':
                    self.add_checkin('stop', 'sport')
                    text = 'Активность "Спорт" была завершена!'

                self.result = Response(text, buttons, session_state=1)
                return

            if self.command == 'activity_work':
                self.add_checkin('start', 'work')
                text = 'Принято! Отслеживаю активность "Работа"'
            elif self.command == 'activity_homework':
                self.add_checkin('start', 'homework')
                text = 'Принято! Отслеживаю активность "Домашние дела"'
            elif self.command == 'activity_hobby':
                self.add_checkin('start', 'hobby')
                text = 'Принято! Отслеживаю активность "хобби"'
            elif self.command == 'activity_sport':
                self.add_checkin('start', 'sport')
                text = 'Принято! Отслеживаю активность "Спорт"'

            self.result = Response(text, buttons, session_state=1)
                
        elif self.session_state == 4:
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
        text = TEXTS['command_not_found']
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

    def activities(self):
        text = TEXTS['activities']
        self.result = Response(text, session_state=2)

    def add_checkin(self, type, checkin_type):
        db = DatabaseManager('checkins.db')
        current_time = self.get_time()
        db.insert_checkin(self.__user_id, current_time, type, checkin_type)

    def get_checkins(self):
        db = DatabaseManager('checkins.db')
        self.checkins = db.select_checkins(self.__user_id)

    def help(self):
        """ Помощь пользователю """
        text = TEXTS['help']
        buttons = HELP_BUTTONS
        self.result = Response(text, buttons, session_state=4)

    def about_skill(self):
        text = TEXTS['about_skill']
        buttons = HELP_BUTTONS
        self.result = Response(text, buttons, session_state=4)

    def about_activities(self):
        text = TEXTS['about_activities']
        buttons = HELP_BUTTONS
        self.result = Response(text, buttons, session_state=4)

    def about_statistic(self):
        text = TEXTS['about_statistic']
        buttons = HELP_BUTTONS
        self.result = Response(text, buttons, session_state=4)

    def get_time(self, time=None, return_timestamp=False):
        tz = pytz.timezone(self.timezone)
        if time:
            return dt.strptime(time, '%d-%m-%Y %H:%M:%S')
        
        if return_timestamp:
            current_time = dt.strftime(dt.now(tz), '%d-%m-%Y %H:%M:%S')
            return dt.strptime(current_time, '%d-%m-%Y %H:%M:%S')
            
        return dt.strftime(dt.now(tz), '%d-%m-%Y %H:%M:%S')
