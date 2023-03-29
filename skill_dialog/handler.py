from skill_requests.Response import Response
from database.manage import DatabaseManager
from .skill_buttons import MAIN_MENU_BUTTONS, HELP_BUTTONS, \
    ACTIVITY_TYPES, END_ACTIVITY, STATISTIC_BUTTONS, ENTRIES_BUTTONS_START, \
    ENTRIES_BUTTONS, ENTRIES_BUTTONS_END, ENTRIES_ONLY_ONE_PAGE, STATISTIC_ACTIVITIES_CARD, \
    WHAT_YOU_CAN_CARD, POSSIBILITIES_BUTTONS, MAIN_MENU_CARD, HELLO_NEW_BUTTONS, \
    ACTIVITIES_CARD, ABOUT_SKILL_CARD, ABOUT_ACTIVITIES_CARD, ABOUT_STATISTIC_CARD

from .skill_texts import TEXTS
from datetime import datetime as dt
import pytz
import random
from uuid import uuid4


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

        if self.command in ('none', 'None', None):
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
                    self.close_activity(confirm_state_std=True)
                    return

                self.activities()

            elif self.command == 'statistic':
                self.statistic()

            elif self.command == 'what_you_can':
                self.about_possibilities()

            elif self.command == 'dev':
                db = DatabaseManager()
                start_time = self.get_time(return_timestamp=True, tz_m=True)
                end_time = start_time + pytz.HOUR
                start_time = dt.strftime(start_time, '%d-%m-%Y %H:%M:%S')
                end_time = dt.strftime(end_time, '%d-%m-%Y %H:%M:%S')
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

            elif self.command == 'dev_info':
                text = (
                    '1) Для Вашего удобства существует кнопка добавления записи об активности\n'
                    '2) Активность "Прочее" ещё не готова (как и произвольный текст к активностям)\n'
                    '3) Отключено определение часового пояса на время проверки. '
                    'Используется часовой пояс по умолчанию (Europe/Moscow)\n'
                    '4) В статистике существует пагинация (5 записей на страничку)\n'
                    '5) В статистике не готова визуализация, но жмякнуть кнопку (возможно) стоит\n'
                    '6) В планах добавить статистику за неделю (сейчас ограничено сутками)\n'
                    '7) Надеемся, что информации в разделе помощь или что ты умеешь будет достаточно\n'
                    'Приятного пользования!'
                )
                buttons = [
                    {
                        'title': 'Назад',
                        'payload': 'back',
                        'hide': False
                    }
                ]

                self.result = Response(text, buttons, session_state=666, tts='')

        # dev help
        elif self.session_state == 666:
            self.main_menu()

        # Раздел активностей
        elif self.session_state == 2:
            buttons = MAIN_MENU_BUTTONS
            self.set_activity_name(self.command)
            if self.command == 'back':
                self.main_menu()
                return

            if self.checkins_list and len(self.checkins_list) % 2 == 1:
                self.close_activity(confirm_state_std=True)
                return

            checkin_id = str(uuid4())

            self.add_checkin(checkin_id, 'start', self.command)
            text = (
                f'Принято! Отслеживаю активность "{self.activity_name}". '
                'Когда Вы закончите, просто сообщите об этом. '
            )

            tts = f"{text}{TEXTS['main_menu']}"
            card = MAIN_MENU_CARD
            card['header'].update({'text': text})
            self.result = Response('', buttons, card, session_state=1, tts=tts)

        elif self.session_state == 21:
            if self.command == 'close_activity':
                self.close_activity()

            elif self.command == 'continue_activity':
                self.main_menu()

        elif self.session_state == 22:
            if self.command == 'close_activity':
                db = DatabaseManager()
                db.delete_last_checkin(self.__user_id, self.checkins_list[0][0])
                text = 'Активность не была сохранена из-за короткой продолжительности. ' \
                       'Хотите начать новую активность или посмотреть статистику?'
                card = MAIN_MENU_CARD
                card['header'].update({'text': text})
                buttons = MAIN_MENU_BUTTONS
                self.result = Response('', buttons, card, session_state=1, tts=text)

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
                text = 'Конечно же это не реализовано. Важнейшая фишка навыка не реализована. ' \
                       'Прекрасно. Но всё же. До встречи в итоговой версии!'
                tts = 'sil <[250]> Конечно же это не реализовано. sil <[750]>  Важнейшая фишка навыка не ' \
                      'реализована. sil <[750]>' \
                      'Зато несколько дней было потрачено на деплой навыка во всевозможных ' \
                      'местах. sil <[750]> Прекрасно. sil <[750]> Но всё же. sil <[300]>' \
                      'До встречи в итоговой версии!'
                card = MAIN_MENU_CARD
                card['header'].update({'text': text})
                self.result = Response(text, MAIN_MENU_BUTTONS, card, session_state=1, tts=tts)

            elif self.command in ['back', 'back_to_menu']:
                self.main_menu()

        # Раздел статистики (Активности)
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
                    self.result = Response(
                        text, ENTRIES_BUTTONS, activities_card,
                        session_state=self.session_state + 1
                    )

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

        # Раздел статистики (Визуализация)
        elif self.session_state == 30:
            text = 'Not realized'
            buttons = MAIN_MENU_BUTTONS
            self.result = Response(text, buttons, session_state=1)

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
            db.insert_user(self.__user_id, 'Denis')

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
        tts = 'sil <[250]> Если хотите начать или закончить активность - скажите "Активность". ' \
              'sil <[250]> Хотите узнать свою статистику? Скажите "Статистика" и я покажу её вам. ' \
              'sil <[250]> Скажите "Помощь", если хотите узнать о навыке больше'

        if new_session:
            text = 'Привет! ' + text
            tts = 'Привет! ' + tts

        buttons = MAIN_MENU_BUTTONS
        card = MAIN_MENU_CARD
        card['header'].update({'text': text})
        self.result = Response('', buttons, card,
                               session_state=1, tts=tts)

    # Что ты умеешь
    def about_possibilities(self):
        """ Краткая информация о навыке """
        text = 'О чём именно вы хотите узнать? (P.S. BigImage реально Big)'
        tts = TEXTS['what_you_can']
        buttons = POSSIBILITIES_BUTTONS
        card = WHAT_YOU_CAN_CARD
        card['header'].update({'text': text})
        self.result = Response(text, buttons, card,
                               session_state=4, tts=tts)

    # Активности
    def activities(self):
        text = random.choice(TEXTS['activities_rand'])
        tts = text + TEXTS['activities']
        buttons = ACTIVITY_TYPES
        card = ACTIVITIES_CARD
        card['header'].update({'text': text})
        self.result = Response('', buttons, card, session_state=2, tts=tts)

    def statistic(self):
        self.get_activities()
        text = 'Хотите увидеть визуализацию или посмотреть записи об Активностях?'
        buttons = STATISTIC_BUTTONS

        if not self.activities_list:
            text = 'Похоже, сегодня Вы ещё не закончили ни одной активности! '
            tts = f'{text}{TEXTS["main_menu"]}'
            buttons = MAIN_MENU_BUTTONS
            card = MAIN_MENU_CARD
            card['header'].update({'text': text})
            self.result = Response('', buttons, card, session_state=1, tts=tts)
            return

        self.result = Response(text, buttons, session_state=3)

    def get_activities_card(self, start):
        activity_items = []
        self.get_activities()
        entries_count = len(self.activities_list)
        last_page = False
        if entries_count <= start + 5:
            last_page = True

        for row in self.activities_list[start:start + 5]:
            activity_type = row[-2]
            self.set_activity_name(activity_type)
            start_time = dt.strptime(row[3], '%d-%m-%Y %H:%M:%S')
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

    def add_checkin(self, checkin_id, checkin_type, activity_type):
        db = DatabaseManager()
        current_time = self.get_time()
        db.insert_checkin(checkin_id, self.__user_id, current_time, checkin_type, activity_type)

    def get_checkins(self):
        db = DatabaseManager()
        today_date = dt.strftime(dt.date(self.get_time(return_timestamp=True, tz_m=True)), '%d-%m-%Y')
        self.checkins_list = db.select_checkins(self.__user_id, today_date)

    def add_activity(self, general_id, activity_id, start_time, end_time, duration,
                     activity_type, text):
        db = DatabaseManager()
        db.insert_activity(general_id, self.__user_id, activity_id, start_time, end_time,
                           duration, activity_type, text)

    def get_activities(self):
        db = DatabaseManager()
        today_date = dt.strftime(dt.date(self.get_time(return_timestamp=True, tz_m=True)), '%d-%m-%Y')
        self.activities_list = db.select_activities(self.__user_id, today_date)

    def close_activity(self, confirm_state_std=False):
        self.set_activity_name(self.checkins_list[0][-1])
        self.get_activities()
        buttons = MAIN_MENU_BUTTONS
        checkin_id = str(uuid4())
        start_time = self.checkins_list[0][1]
        start_time = self.get_time(start_time)
        current_time = self.get_time(return_timestamp=True)
        activity_duration = current_time - start_time
        activity_duration = int(activity_duration.total_seconds())
        start_time_write = dt.strftime(start_time, '%d-%m-%Y %H:%M:%S')
        start_time_show = dt.strftime(start_time, '%H:%M:%S')
        current_time = dt.strftime(current_time, '%d-%m-%Y %H:%M:%S')
        activity_id = 0
        general_activity_id = str(uuid4())
        activity_duration_date = self.get_time(timestamp=activity_duration)

        if activity_duration < 60:
            activity_duration_date = 'меньше минуты'

        if confirm_state_std:
            text = f'Активность: {self.activity_name} \nНачало: {start_time_show}\n' \
                   f'Продолжительность: {activity_duration_date}\nХотите завершить активность?"'
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

        if self.activities_list:
            activity_id = self.activities_list[0][2] + 1

        self.add_activity(general_activity_id, activity_id, start_time_write, current_time, activity_duration,
                          self.checkins_list[0][3], 'text')
        self.add_checkin(checkin_id, 'stop', self.checkins_list[0][3])
        text = f'Активность "{self.activity_name}" была завершена!'
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
    def get_time(time=None, return_timestamp=False, timestamp=None, tz_m=False):
        """ Возвращает текущее время, либо преобразует str в timestamp """
        # tz = pytz.timezone(self.timezone) ВЕРНУТЬ В РЕЛИЗЕ
        tz = pytz.timezone('Europe/Moscow')
        if tz_m:
            tz = pytz.timezone('Europe/Moscow')
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
