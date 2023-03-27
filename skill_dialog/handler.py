from skill_requests.Response import Response
from database.manage import DatabaseManager
from .skill_buttons import SKILL_BUTTONS, MAIN_MENU_BUTTONS, HELP_BUTTONS, \
    ACTIVITY_TYPES, END_ACTIVITY, STATISTIC_BUTTONS, ENTRIES_BUTTONS_START, \
    ENTRIES_BUTTONS, ENTRIES_BUTTONS_END, ENTRIES_ONLY_ONE_PAGE, ACTIVITIES_CARD
from .skill_texts import TEXTS
from datetime import datetime as dt
import pytz
import random


# state 1: выбор функции
# state 2: переключение на нужную функцию


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
        self.activity_name = None
        self.result = None

        self.check_user_is_new()
        self.get_checkins()

    def process(self):
        """ Обработка команды """
        if self.session_is_new:
            self.new_session()
            return

        if self.command in ('none', 'None'):
            self.command_not_found()
            return

        # Главное меню
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
                if self.checkins_list and len(self.checkins_list) % 2 == 1:
                    self.close_activity(confirm_state=True)
                    return

                self.activities()

            elif self.command == 'statistic':
                self.statistic()

        # Раздел активностей
        elif self.session_state == 2:
            buttons = MAIN_MENU_BUTTONS
            self.set_activity_name(self.command)
            if self.command == 'back':
                self.main_menu()
                return

            if self.checkins_list and len(self.checkins_list) % 2 == 1:
                self.close_activity(confirm_state=True)
                return

            if not self.checkins_list:
                checkin_id = 0
            else:
                checkin_id = self.checkins_list[-1][0][0] + 1

            self.add_checkin(checkin_id, 'start', self.command)
            text = (
                f'Принято! Отслеживаю активность "{self.activity_name}" '
                f'Когда Вы закончите, просто сообщите об этом!'
            )
            self.result = Response(text, buttons, session_state=1)

        elif self.session_state == 21:
            if self.command == 'close_activity':
                self.close_activity()

            elif self.command == 'continue_activity':
                self.main_menu()

        elif self.session_state == 3:
            self.get_activities()
            if self.command == 'get_entries':
                text = ''
                activities_card, last_page = self.get_activities_card(0)
                if last_page:
                    self.result = Response('', ENTRIES_ONLY_ONE_PAGE, activities_card, session_state=3)
                    return

                self.result = Response(text, ENTRIES_BUTTONS_START, activities_card, session_state=31)

            elif self.command == 'get_visualisation':
                text = 'Конечно же это не реализовано. Хотите добавить активность или узнать статистику?'
                self.result = Response(text, MAIN_MENU_BUTTONS, session_state=1)

            elif self.command in ['back', 'back_to_menu']:
                self.result = Response(TEXTS['main_menu'], MAIN_MENU_BUTTONS, session_state=1)

        # Раздел статистики (Активности)
        elif self.session_state >= 31:
            print(self.command)
            if self.command == 'entries_continue':
                text = ''
                start = 5 * (self.session_state - 30)
                activities_card, last_page = self.get_activities_card(start)
                if last_page:
                    self.result = Response(TEXTS['main_menu'], ENTRIES_BUTTONS_END, activities_card,
                                           session_state=self.session_state)
                    return
                else:
                    self.result = Response(
                        text, ENTRIES_BUTTONS, activities_card,
                        session_state=self.session_state + 1
                    )

            elif self.command == 'entries_previous' and self.session_state == 32:
                print('work')
                text = ''
                activities_card, _ = self.get_activities_card(0)
                self.result = Response(text, ENTRIES_BUTTONS_START, activities_card,
                                       session_state=31)

            elif self.command == 'entries_previous':
                print('1wokrs')
                text = ''
                start = 5 * (self.session_state - 31)
                activities_card, _ = self.get_activities_card(start)
                self.result = Response(text, ENTRIES_BUTTONS, activities_card,
                                       session_state=self.session_state-1)

            elif self.command in ['entries_stop', 'no', 'back_to_menu']:
                self.main_menu()

        # Раздел статистики (Визуализация)
        elif self.session_state == 30:
            text = 'Not realized'
            buttons = MAIN_MENU_BUTTONS
            self.result = Response(text, buttons, session_state=1)

        # Раздел помощи
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
        db = DatabaseManager()
        self.user_exists = db.check_user_exists(self.__user_id)
        if not self.user_exists:
            db.insert_user(self.__user_id, 'Denis')

    def respond(self):
        return self.result.respond()

    # Функции диалога
    def new_session(self):
        """ Новая сессия в навыке """
        if self.user_exists:
            text = random.choice(TEXTS['hello_std'])
            buttons = MAIN_MENU_BUTTONS

        else:
            text = TEXTS['hello_new']
            buttons = [SKILL_BUTTONS['hello_new']]

        self.result = Response(text, buttons, session_state=1)

    # Меню
    def main_menu(self):
        """ Главаное меню навыка """
        text = TEXTS['main_menu']
        buttons = MAIN_MENU_BUTTONS
        self.result = Response(text, buttons, session_state=1)

    # Активности
    def activities(self):
        text = TEXTS['activities']
        buttons = ACTIVITY_TYPES
        self.result = Response(text, buttons, session_state=2)

    def statistic(self):
        self.get_activities()
        text = 'Хотите увидеть визуализацию, или показать записи об Активностях?'
        buttons = STATISTIC_BUTTONS

        if not self.activities_list:
            text = 'Похоже, сегодня Вы ещё не закончили ни одной активности!'
            self.result = Response(text, MAIN_MENU_BUTTONS, session_state=1)
            return

        self.result = Response(text, buttons, session_state=3)

    def get_activities_card(self, start):
        activity_items = []
        self.get_activities()
        entries_count = len(self.activities_list)
        max_page_count = entries_count // 5
        current_page = start // 5
        last_page = False
        if entries_count < start + 5:
            last_page = True

        for row in self.activities_list[start:start + 5]:
            values = row[0]
            activity_type = values[-2]
            self.set_activity_name(activity_type)
            start_time = dt.strptime(values[3], '%d-%m-%Y %H:%M:%S')
            start_time = dt.strftime(start_time, '%H:%M:%S')
            duration = self.get_time(timestamp=values[5])

            if activity_type == 'activity_work':
                image_id = '213044/39799b3319bd0fb5135b'
                title = 'Работа'
                desctiption = f'Начало: {start_time} | Продолжительность {duration}'
            elif activity_type == 'activity_homework':
                image_id = '213044/1ad7f49599385016222d'
                title = 'Домашние Дела'
                desctiption = f'Начало: {start_time} | Продолжительность {duration}'
            elif activity_type == 'activity_hobby':
                image_id = '213044/b85af62b5e29b538daca'
                title = 'Хобби'
                desctiption = f'Начало: {start_time} | Продолжительность {duration}'
            elif activity_type == 'activity_sport':
                image_id = '213044/d458652c075b18128692'
                title = 'Спорт'
                desctiption = f'Начало: {start_time} | Продолжительность {duration}'
            else:
                image_id = '213044/40740b20816d29f6406b'
                title = 'Неизвестно'
                desctiption = f'Начало: {start_time} | Продолжительность {duration}'

            activity_item = {
                'image_id': image_id,
                'title': title,
                'description': desctiption
            }

            activity_items.append(activity_item)

        self.session_state += 1
        activities_card = ACTIVITIES_CARD
        activities_card.update({'items': activity_items})
        return activities_card, last_page

    def add_checkin(self, checkin_id, checkin_type, activity_type):
        db = DatabaseManager()
        current_time = self.get_time()
        db.insert_checkin(checkin_id, self.__user_id, current_time, checkin_type, activity_type)

    def get_checkins(self):
        db = DatabaseManager()
        self.checkins_list = db.select_checkins(self.__user_id)

    def add_activity(self, general_id, activity_id, start_time, end_time, duration,
                     activity_type, text):
        db = DatabaseManager()
        db.insert_activity(general_id, self.__user_id, activity_id, start_time, end_time,
                           duration, activity_type, text)

    def get_activities(self):
        db = DatabaseManager()
        today_date = dt.strftime(dt.date(self.get_time(return_timestamp=True)), '%d-%m-%Y')
        self.activities_list = db.select_activities(self.__user_id, today_date)

    def close_activity(self, confirm_state=False):
        self.set_activity_name(self.checkins_list[-1][0][-1])
        self.get_activities()
        buttons = MAIN_MENU_BUTTONS

        checkin_id = self.checkins_list[-1][0][0] + 1
        start_time = self.checkins_list[-1][0][1]
        start_time = self.get_time(start_time)
        current_time = self.get_time(return_timestamp=True)
        activity_duration = current_time - start_time
        activity_duration = int(activity_duration.total_seconds())
        start_time = dt.strftime(start_time, '%d-%m-%Y %H:%M:%S')
        current_time = dt.strftime(current_time, '%d-%m-%Y %H:%M:%S')

        activity_id = 0
        general_activity_id = 0

        activity_duration_date = self.get_time(timestamp=activity_duration)

        if confirm_state:
            text = f'Активность: {self.activity_name} \nНачало: {start_time}\n' \
                   f'Продолжительность: {activity_duration_date}\nХотите завершить активность?"'
            buttons = END_ACTIVITY
            self.result = Response(text, buttons, session_state=21)
            return

        if self.activities_list:
            activity_id = self.activities_list[-1][0][2] + 1
            general_activity_id = self.activities_list[-1][0][0] + 1

        self.add_activity(general_activity_id, activity_id, start_time, current_time, activity_duration,
                          self.checkins_list[-1][0][3], 'text')
        self.add_checkin(checkin_id, 'stop', self.checkins_list[-1][0][3])
        text = f'Активность "{self.activity_name}" была завершена!'

        self.result = Response(text, buttons, session_state=1)
        return

    # Помощь
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

    def get_time(self, time=None, return_timestamp=False, timestamp=None):
        """ Возвращает текущее время, либо преобразует str в timestamp """
        tz = pytz.timezone(self.timezone)
        if time:
            return dt.strptime(time, '%d-%m-%Y %H:%M:%S')

        if return_timestamp:
            current_time = dt.strftime(dt.now(tz), '%d-%m-%Y %H:%M:%S')
            return dt.strptime(current_time, '%d-%m-%Y %H:%M:%S')

        if timestamp:
            datetime_from_timestamp = dt.fromtimestamp(float(timestamp))
            return dt.strftime(datetime_from_timestamp, '%H:%M:%S')

        return dt.strftime(dt.now(tz), '%d-%m-%Y %H:%M:%S')

    def set_activity_name(self, activity_type):
        if activity_type == 'activity_work':
            self.activity_name = 'Работа'
        elif activity_type == 'activity_homework':
            self.activity_name = 'Домашние Дела'
        elif activity_type == 'activity_hobby':
            self.activity_name = 'Хобби'
        elif activity_type == 'activity_sport':
            self.activity_name = 'Спорт'
