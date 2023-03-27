DOMEN = 'https://4dfa-83-220-236-37.eu.ngrok.io'

# Кнопки навыка
SKILL_BUTTONS = {
    # About
    'help': {
        'title': '\U0001F4D6 Помощь',
        'payload': ['help'],
        'hide': False
    },
    'about_skill': {
        'title': '\U0001F4D6 О навыке',
        'payload': ['about_skill'],
        'hide': False
    },
    'about_activities': {
        'title': '\U0001F4D6 Об активностях',
        'payload': ['about_activities'],
        'hide': False
    },
    'about_statistic': {
        'title': '\U0001F4D6 О статистике',
        'payload': ['about_statistic'],
        'hide': False
    },

    # Activities
    'activities': {
        'title': '\U00002705 Активности',
        'payload': ['activities'],
        'hide': False
    },
    'create_activity': {
        'title': 'Отметиться',
        'payload': ['checkin'],
        'hide': False
    },

    'activity_work': {
        'title': '\U0001F4BC Работа',
        'payload': ['activity_work'],
        'hide': False
    },

    'activity_homework': {
        'title': '\U0001F3E0 Домашние Дела',
        'payload': ['activity_homework'],
        'hide': False
    },

    'activity_hobby': {
        'title': '\U0001f3ae Хобби',
        'payload': ['activity_hobby'],
        'hide': False
    },

    'activity_sport': {
        'title': '\U0001F3BE Спорт',
        'payload': ['activity_sport'],
        'hide': False
    },

    'activity_work_hide': {
        'title': 'Работа',
        'payload': ['activity_work'],
        'hide': True
    },

    'activity_homework_hide': {
        'title': 'Домашние Дела',
        'payload': ['activity_homework'],
        'hide': True
    },

    'activity_hobby_hide': {
        'title': 'Хобби',
        'payload': ['activity_hobby'],
        'hide': True
    },

    'activity_sport_hide': {
        'title': 'Спорт',
        'payload': ['activity_sport'],
        'hide': True
    },

    'activity_end_yes': {
        'title': '\U00002705 Завершить активность',
        'payload': ['close_activity'],
        'hide': False
    },
    
    'activity_end_no': {
        'title': '\U0000274C Отмена',
        'payload': ['continue_activity'],
        'hide': False
    },

    'activity_end_yes_hide': {
        'title': 'Завершить активность',
        'payload': ['close_activity'],
        'hide': True
    },
    
    'activity_end_no_hide': {
        'title': 'Отмена',
        'payload': ['continue_activity'],
        'hide': True
    },

    # Statistic
    'statistic': {
        'title': '\U0001F4CA Статистика',
        'payload': ['statistic'],
        'hide': False
    },

    'get_visualisation': {
        'title': 'Визуализация',
        'payload': ['get_visualisation'],
        'hide': False
    },

    'get_entries': {
        'title': 'Список активностей',
        'payload': ['get_entries', None],
        'hide': False
    },

    'entries_continue': {
        'title': 'Следующая страница',
        'payload': ['entries_continue'],
        'hide': False
    },

    'entries_previous': {
        'title': 'Предыдущая страница',
        'payload': ['entries_previous'],
        'hide': False
    },

    'entries_stop': {
        'title': 'Главное меню',
        'payload': ['entries_stop'],
        'hide': False
    },

    # Hello
    'hello_new': {
        'title': '\U0001F525 Поехали',
        'payload': ['yes'],
        'hide': False
    },

    'back': {
        'title': '\U0001F519 Назад',
        'payload': ['back'],
        'hide': False
    }
}


ACTIVITIES_CARD = {
    'type': 'ItemsList',
    'header': {
        'text': 'Ваши Активности'
    },
    'items': {

    }
}

ACTIVITY_ITEM = {
    'image_id': None,
    'title': None,
    'description': None
}

MAIN_MENU_BUTTONS = [
    SKILL_BUTTONS['activities'],
    SKILL_BUTTONS['statistic'],
    SKILL_BUTTONS['help']
]

HELP_BUTTONS = [
    SKILL_BUTTONS['about_skill'],
    SKILL_BUTTONS['about_activities'],
    SKILL_BUTTONS['about_statistic'],
    SKILL_BUTTONS['back']
]

ACTIVITY_TYPES = [
    SKILL_BUTTONS['activity_work'],
    SKILL_BUTTONS['activity_homework'],
    SKILL_BUTTONS['activity_hobby'],
    SKILL_BUTTONS['activity_sport'],
    SKILL_BUTTONS['activity_work_hide'],
    SKILL_BUTTONS['activity_homework_hide'],
    SKILL_BUTTONS['activity_hobby_hide'],
    SKILL_BUTTONS['activity_sport_hide'],
    SKILL_BUTTONS['back']
]

END_ACTIVITY = [
    SKILL_BUTTONS['activity_end_yes'],
    SKILL_BUTTONS['activity_end_no'],
    SKILL_BUTTONS['activity_end_yes_hide'],
    SKILL_BUTTONS['activity_end_no_hide']
]

STATISTIC_BUTTONS = [
    SKILL_BUTTONS['get_visualisation'],
    SKILL_BUTTONS['get_entries'],
    SKILL_BUTTONS['back']
]

ENTRIES_BUTTONS_START = [
    SKILL_BUTTONS['entries_continue'],
    SKILL_BUTTONS['entries_stop']
]

ENTRIES_BUTTONS = [
    SKILL_BUTTONS['entries_continue'],
    SKILL_BUTTONS['entries_previous'],
    SKILL_BUTTONS['entries_stop']
]

ENTRIES_BUTTONS_END = [
    SKILL_BUTTONS['entries_previous'],
    SKILL_BUTTONS['entries_stop']
]

ENTRIES_ONLY_ONE_PAGE = [
    SKILL_BUTTONS['back']
]
