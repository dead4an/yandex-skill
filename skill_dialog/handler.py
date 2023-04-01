import time

from skill_requests.Response import Response
from database.manage import DatabaseManager
from .skill_texts import TEXTS
from datetime import datetime as dt
import pytz
import random
from uuid import uuid4
from .skill_buttons import (MAIN_MENU_BUTTONS, HELP_BUTTONS,
                            ACTIVITY_TYPES, END_ACTIVITY, STATISTIC_BUTTONS, ENTRIES_BUTTONS_START,
                            ENTRIES_BUTTONS, ENTRIES_BUTTONS_END, ENTRIES_ONLY_ONE_PAGE, STATISTIC_ACTIVITIES_CARD,
                            WHAT_YOU_CAN_CARD, POSSIBILITIES_BUTTONS, MAIN_MENU_CARD, HELLO_NEW_BUTTONS,
                            ACTIVITIES_CARD, ABOUT_SKILL_CARD, ABOUT_ACTIVITIES_CARD, ABOUT_STATISTIC_CARD,
                            DAILY_STATISTIC_CARD)


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
        self.last_checkin = None
        self.activities_list = None
        self.activity_name = None
        self.result = None
        self.check_user_is_new()

    def process(self):
        """ Обработка команды """
        if self.session_is_new:
            if self.command is None:
                self.new_session()

            elif self.command == 'activities':
                self.activities()

            elif self.command == 'statistic':
                self.statistic()

        elif self.command is None:
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
                self.get_last_checkin()
                if self.last_checkin and self.last_checkin['checkin_type'] == 'start':
                    self.close_activity(confirm_state_std=True)
                    return

                self.activities()

            elif self.command == 'close_activity':
                self.activities()

            elif self.command == 'statistic':
                self.statistic()

            elif self.command == 'what_you_can':
                self.about_possibilities()

            elif self.command == 'dev':
                db = DatabaseManager()
                start_time = self.get_time(return_timestamp=True)
                end_time = start_time + pytz.HOUR
                start_time = dt.strftime(start_time, '%Y-%m-%d %H:%M:%S')
                end_time = dt.strftime(end_time, '%Y-%m-%d %H:%M:%S')
                db.insert_activity(
                    id=str(uuid4()), user_id=self.__user_id, activity_id=1,
                    start_time=start_time, end_time=end_time, duration=3600, activity_type='activity_work',
                    text='dev'
                )

                text = 'DEV: Активность добавлена'
                card = MAIN_MENU_CARD
                card['header'].update({'text': text})
                buttons = MAIN_MENU_BUTTONS
                self.result = Response('', buttons, card, session_state=1, tts='Читер!')

        # Раздел активностей
        elif self.session_state == 2:
            self.set_activity_name(self.command)
            if self.command == 'back':
                self.main_menu()
                return

            if self.command == 'statistic':
                self.statistic()
                return

            checkin_id = str(uuid4())

            self.add_checkin(checkin_id, 'start', self.command)
            print(self.command)
            text = (
                f'Принято! Отслеживаю активность "{self.activity_name}". '
                'Когда Вы закончите, просто сообщите об этом. '
            )

            tts = f"{text}{TEXTS['main_menu']}"
            buttons = MAIN_MENU_BUTTONS
            card = MAIN_MENU_CARD
            card['header'].update({'text': text})
            self.result = Response('', buttons, card, session_state=1, tts=tts)

        # Завершение активности (подтверждение)
        elif self.session_state == 21:
            if self.command == 'close_activity':
                self.close_activity()

            elif self.command == 'continue_activity':
                self.main_menu()

        elif self.session_state == 22:
            if self.command == 'close_activity':
                self.get_last_checkin()
                db = DatabaseManager()
                db.delete_last_checkin(self.__user_id, self.last_checkin['id'])
                text = 'Активность не была сохранена из-за короткой продолжительности. ' \
                       'Хотите начать новую активность или посмотреть статистику?'
                card = MAIN_MENU_CARD
                card['header'].update({'text': text})
                buttons = MAIN_MENU_BUTTONS
                self.result = Response('', buttons, card, session_state=1, tts=text)

            elif self.command == 'continue_activity':
                self.main_menu()

        # Просмотр статистики
        elif self.session_state == 3:
            if self.command == 'get_entries':
                text = ''
                activities_card, last_page = self.get_activities_card(0)
                if last_page:
                    self.result = Response('', ENTRIES_ONLY_ONE_PAGE, activities_card, session_state=3)
                    return

                self.result = Response(text, ENTRIES_BUTTONS_START, activities_card, session_state=31)

            elif self.command == 'get_daily_statistic':
                self.get_daily_activities_card()

            elif self.command == 'get_weekly_statistic':
                self.main_menu()

            elif self.command in ['back', 'back_to_menu']:
                self.main_menu()

            elif self.command == 'activities':
                self.activities()

        # Просмотр подробной статистики за день
        elif self.session_state >= 31:
            if self.command == 'entries_continue':
                text = ''
                start = 5 * (self.session_state - 30)
                activities_card, last_page = self.get_activities_card(start)
                if last_page:
                    self.result = Response(TEXTS['main_menu'], ENTRIES_BUTTONS_END, activities_card,
                                           session_state=self.session_state + 1)
                    return
                else:
                    self.result = Response(text, ENTRIES_BUTTONS, activities_card,
                                           session_state=self.session_state + 1)

            elif self.command == 'entries_previous' and self.session_state == 32:
                text = ''
                activities_card, _ = self.get_activities_card(0)
                self.result = Response(text, ENTRIES_BUTTONS_START, activities_card,
                                       session_state=31)

            elif self.command == 'entries_previous':
                text = ''
                start = 5 * (self.session_state - 32)
                activities_card, _ = self.get_activities_card(start)
                self.result = Response(text, ENTRIES_BUTTONS, activities_card,
                                       session_state=self.session_state - 1)

            elif self.command in ['entries_stop', 'no', 'back_to_menu']:
                self.main_menu()

        # Что ты умеешь
        elif self.session_state == 4:
            if self.command == 'about_skill':
                self.about_skill()
            elif self.command == 'about_activities':
                self.about_activities()
            elif self.command == 'about_statistic':
                self.about_statistic()
            elif self.command in 'back' or 'back_to_menu':
                self.main_menu()

        # Раздел помощи (зацикленный + выход в меню)
        elif self.session_state == 6:
            if self.command == 'about_skill':
                self.about_skill()
            elif self.command == 'about_activities':
                self.about_activities()
            elif self.command == 'about_statistic':
                self.about_statistic()
            elif self.command in 'back' or 'back_to_menu':
                self.main_menu()

        # Статистика за день
        elif self.session_state == 7:
            self.main_menu()

    def command_not_found(self):
        """ Команда не найдена """
        text = TEXTS['command_not_found']
        buttons = MAIN_MENU_BUTTONS
        card = MAIN_MENU_CARD
        card['header'].update({'text': text})
        self.result = Response('', buttons, card, session_state=1, tts=text)

    def check_user_is_new(self):
        """ Проверка нового пользователя """
        db = DatabaseManager()
        self.user_exists = db.check_user_exists(self.__user_id)
        if not self.user_exists:
            db.insert_user(self.__user_id)

    def respond(self):
        return self.result.respond()

    # Функции диалога
    def new_session(self):
        """ Новая сессия в навыке """
        if self.user_exists:
            self.main_menu(new_session=True)

        else:
            text = TEXTS['hello_new']
            buttons = HELLO_NEW_BUTTONS
            self.result = Response(text, buttons, session_state=1)

    # Меню
    def main_menu(self, new_session=False):
        """ Главаное меню навыка """
        text = random.choice(TEXTS['hello_std'])
        tts = 'Если хотите начать или закончить активность - скажите "Активность". ' \
              'sil <[250]> Хотите узнать свою статистику? Скажите "Статистика" и я покажу её вам. ' \
              'sil <[250]> Скажите "Помощь", если хотите узнать о навыке больше'

        if new_session:
            timestamp = self.get_time(return_timestamp=True)
            timestamp = time.mktime(timestamp.timetuple())
            timestamp = self.get_time(timestamp=timestamp)

            if '00:00:00' <= timestamp <= '05:59:59':
                time_name = 'Доброй ночи! '
            elif '06:00:00' <= timestamp <= '11:59:59':
                time_name = 'Доброе утро! '
            elif '12:00:00' <= timestamp <= '17:59:59':
                time_name = 'Добрый день! '
            else:
                time_name = 'Добрый вечер! '

            text = time_name + text
            tts = time_name + tts

        buttons = MAIN_MENU_BUTTONS
        card = MAIN_MENU_CARD
        card['header'].update({'text': text})
        self.result = Response('', buttons, card,
                               session_state=1, tts=tts)

    # Что ты умеешь
    def about_possibilities(self):
        """ Краткая информация о навыке """
        text = 'О чём именно вы хотите узнать?'
        tts = TEXTS['what_you_can']
        buttons = POSSIBILITIES_BUTTONS
        card = WHAT_YOU_CAN_CARD
        card['header'].update({'text': text})
        self.result = Response(text, buttons, card,
                               session_state=4, tts=tts)

    # Активности
    def activities(self):
        """ Раздел активностей """
        text = random.choice(TEXTS['activities_rand'])
        tts = text + TEXTS['activities']
        buttons = ACTIVITY_TYPES
        card = ACTIVITIES_CARD
        card['header'].update({'text': text})
        self.result = Response('', buttons, card, session_state=2, tts=tts)

    def statistic(self):
        today_date = dt.strftime(dt.date(self.get_time(return_timestamp=True)), '%Y-%m-%d')
        print(today_date)
        db = DatabaseManager()
        if not db.check_activity(self.__user_id, today_date):
            text = 'Похоже, сегодня Вы ещё не закончили ни одной активности! '
            tts = f'{text}{TEXTS["main_menu"]}'
            buttons = MAIN_MENU_BUTTONS
            card = MAIN_MENU_CARD
            card['header'].update({'text': text})
            self.result = Response('', buttons, card, session_state=1, tts=tts)
            return

        text = 'Хотите увидеть визуализацию или посмотреть записи об Активностях?'
        buttons = STATISTIC_BUTTONS
        self.result = Response(text, buttons, session_state=3)

    def get_activities_card(self, start):
        """ Возвращает карточку со списком последних активностей """
        self.get_activities()
        activity_items = []
        entries_count = len(self.activities_list)
        last_page = False
        if entries_count <= start + 5:
            last_page = True

        for row in self.activities_list[start:start + 5]:
            activity_type = row[-2]
            self.set_activity_name(activity_type)
            start_time = dt.strptime(row[3], '%Y-%m-%d %H:%M:%S')
            start_time = dt.strftime(start_time, '%H:%M:%S')
            duration = self.get_time(timestamp=row[-3])

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
            elif activity_type == 'activity_other':
                image_id = '213044/d458652c075b18128692'
                title = 'Прочее'
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

        activities_card = STATISTIC_ACTIVITIES_CARD
        activities_card.update({'items': activity_items})
        return activities_card, last_page

    def get_daily_activities_card(self):
        """ Возвращает карточку с общей статистикой за день"""
        self.get_activities()
        activities_duration = {
            'activity_work': 0, 'activity_homework': 0, 'activity_hobby': 0,
            'activity_sport': 0, 'activity_other': 0
        }

        for row in self.activities_list:
            activitity_type = row[-2]
            activity_duration = row[-3]
            activities_duration[activitity_type] += activity_duration

        work_duration = self.get_time(timestamp=activities_duration['activity_work'])
        homework_duration = self.get_time(timestamp=activities_duration['activity_homework'])
        hobby_duration = self.get_time(timestamp=activities_duration['activity_hobby'])
        sport_duration = self.get_time(timestamp=activities_duration['activity_sport'])
        other_duration = self.get_time(timestamp=activities_duration['activity_other'])

        activities_cards = []
        if activities_duration['activity_work']:
            activities_cards.append({
                'image_id': '213044/39799b3319bd0fb5135b',
                'title': 'Работа',
                'description': f'Общее время занятия работой: {work_duration}'
            })
        if activities_duration['activity_homework']:
            activities_cards.append({
                'image_id': '213044/1ad7f49599385016222d',
                'title': 'Домашние Дела',
                'description': f'Общее время занятия домашними делами: {homework_duration}'
            })
        if activities_duration['activity_hobby']:
            activities_cards.append({
                'image_id': '213044/b85af62b5e29b538daca',
                'title': 'Хобби',
                'description': f'Общее время занятия хобби: {hobby_duration}'
            })
        if activities_duration['activity_sport']:
            activities_cards.append({
                'image_id': '213044/d458652c075b18128692',
                'title': 'Спорт',
                'description': f'Общее время занятия спортом: {sport_duration}'
            })
        if activities_duration['activity_other']:
            activities_cards.append({
                'image_id': '1030494/edca956f6dd3f17aa057',
                'title': 'Прочее',
                'description': f'Общее время занятия разными делами: {other_duration}'
            })

        buttons = ENTRIES_ONLY_ONE_PAGE
        daily_card = DAILY_STATISTIC_CARD
        daily_card.update({'items': activities_cards})
        self.result = Response('', buttons, daily_card, session_state=7)

    def add_checkin(self, checkin_id, checkin_type, activity_type):
        """ Добавление отметки о начале | конце активности """
        db = DatabaseManager()
        current_time = self.get_time()
        db.insert_checkin(checkin_id, self.__user_id, current_time, checkin_type, activity_type)

    def get_last_checkin(self):
        """ Возвращает все отметки """
        db = DatabaseManager()
        self.last_checkin = db.select_last_checkin(self.__user_id)

    def add_activity(self, general_id, activity_id, start_time, end_time,
                     duration, activity_type, text):
        """ Добавление записи об активности """
        db = DatabaseManager()
        db.insert_activity(general_id, self.__user_id, activity_id, start_time, end_time,
                           duration, activity_type, text)

    def get_activities(self):
        """ Возвращает все записи об активностях """
        db = DatabaseManager()
        today_date = dt.strftime(dt.date(self.get_time(return_timestamp=True)), '%Y-%m-%d')
        self.activities_list = db.select_activities(self.__user_id, today_date)

    def close_activity(self, confirm_state_std=False):
        self.get_last_checkin()
        self.set_activity_name(self.last_checkin['activity_type'])
        db = DatabaseManager()
        last_activity_id = db.select_last_activity_id(self.__user_id)

        # UUID
        checkin_id = str(uuid4())
        general_activity_id = str(uuid4())

        # Временные преобразования
        activity_start_time = self.last_checkin['start_time']
        activity_start_time = self.get_time(activity_start_time)
        current_time = self.get_time(return_timestamp=True)
        activity_duration = current_time - activity_start_time
        activity_duration = int(activity_duration.total_seconds())
        start_time_write = dt.strftime(activity_start_time, '%Y-%m-%d %H:%M:%S')
        start_time_show = dt.strftime(activity_start_time, '%H:%M:%S')
        current_time = dt.strftime(current_time, '%Y-%m-%d %H:%M:%S')
        activity_duration_timestamp = self.get_time(timestamp=activity_duration)

        if activity_duration < 60:
            activity_duration_timestamp = 'меньше минуты'

        if confirm_state_std:
            text = f'Активность: {self.activity_name} \nНачало: {start_time_show}\n' \
                   f'Продолжительность: {activity_duration_timestamp}\nХотите завершить активность?"'
            buttons = END_ACTIVITY
            self.result = Response(text, buttons, session_state=21)
            return

        if activity_duration < 60:
            text = 'Извините, но продолжительность активности меньше минуты. ' \
                   'Если вы завершите активность сейчас, то она не сохранится. ' \
                   'Хотите завершить активность?'
            buttons = END_ACTIVITY
            self.result = Response(text, buttons, session_state=22)
            return

        self.add_activity(general_activity_id, last_activity_id + 1, start_time_write,
                          current_time, activity_duration, self.last_checkin['activity_type'], 'text')
        self.add_checkin(checkin_id, 'stop', self.last_checkin['activity_type'])
        text = f'Активность "{self.activity_name}" была завершена!'
        buttons = MAIN_MENU_BUTTONS
        card = MAIN_MENU_CARD
        card['header'].update({'text': text})
        tts = f'Активность "{self.activity_name}" была завершена! Если хотите начать ' \
              f'новую активность - скажите "активность". Если хотите посмотреть на статистику, то ' \
              f'скажите "статистика"'
        self.result = Response('', buttons, card, session_state=1, tts=tts)
        return

    # Помощь
    def help(self):
        """ Помощь пользователю """
        tts = TEXTS['help']
        text = 'О чём именно вы хотите узнать? (P.S. BigImage реально Big)'
        buttons = POSSIBILITIES_BUTTONS
        card = WHAT_YOU_CAN_CARD
        card['header'].update({'text': text})
        self.result = Response('', buttons, card, session_state=4, tts=tts)

    def about_skill(self):
        tts = (
            'Этот навык призван помочь Вам следить за тем, как Вы распределяете своё время. Если Вы активная '
            'личность, дорожащая каждой минутой и желающая оценить свои временн+ые затраты - Контроль Времени '
            'обязательно поможет Вам в этом деле. В разделе "Активности" Вы сможете делать отметки о начале и конце '
            'ваших активностей, а раздел "Статистика" предоставит Вам краткую информацию о Ваших активностях в виде '
            'текста и круговой диаграммы. Скажите, если хотите узнать подробнее о статистике и активностях. Или же '
            'вернёмся в главное меню?'
        )
        buttons = HELP_BUTTONS
        card = ABOUT_SKILL_CARD
        self.result = Response('', buttons, card, session_state=6, tts=tts)

    def about_activities(self):
        text = TEXTS['about_activities']
        buttons = HELP_BUTTONS
        card = ABOUT_ACTIVITIES_CARD
        self.result = Response('', buttons, card, session_state=6, tts=text)

    def about_statistic(self):
        text = TEXTS['about_statistic']
        buttons = HELP_BUTTONS
        card = ABOUT_STATISTIC_CARD
        self.result = Response('', buttons, card, session_state=6, tts=text)

    @staticmethod
    def get_time(time=None, return_timestamp=False, timestamp=None):
        """ Возвращает текущее время, либо преобразует str в timestamp """
        # tz = pytz.timezone(self.timezone) ВЕРНУТЬ В РЕЛИЗЕ
        tz = pytz.timezone('Europe/Moscow')
        if time:
            return dt.strptime(time, '%Y-%m-%d %H:%M:%S')

        if return_timestamp:
            current_time = dt.strftime(dt.now(tz), '%Y-%m-%d %H:%M:%S')
            return dt.strptime(current_time, '%Y-%m-%d %H:%M:%S')

        if timestamp:
            datetime_from_timestamp = dt.fromtimestamp(float(timestamp))
            return dt.strftime(datetime_from_timestamp, '%H:%M:%S')

        return dt.strftime(dt.now(tz), '%Y-%m-%d %H:%M:%S')

    def set_activity_name(self, activity_type):
        if activity_type == 'activity_work':
            self.activity_name = 'Работа'
        elif activity_type == 'activity_homework':
            self.activity_name = 'Домашние Дела'
        elif activity_type == 'activity_hobby':
            self.activity_name = 'Хобби'
        elif activity_type == 'activity_sport':
            self.activity_name = 'Спорт'
        elif activity_type == 'activity_other':
            self.activity_name = 'Прочее'
