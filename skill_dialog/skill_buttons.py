DOMEN = 'https://40a2-83-220-236-37.eu.ngrok.io'

# Кнопки навыка
SKILL_BUTTONS = {
    # About
    'help': {
        'title': '\U0001F4D6 Помощь',
        'payload': ['help'],
        'hide': False
    },
    'about_skill': {
        'title': 'О навыке',
        'payload': ['about_skill'],
        'hide': False
    },
    'about_activities': {
        'title': 'Об отметках',
        'payload': ['about_activities'],
        'hide': False
    },
    'about_statistic': {
        'title': 'О статистике',
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
        'title': 'Работа',
        'payload': ['activity_work'],
        'hide': True
    },

    'activity_homework': {
        'title': 'Домашние Дела',
        'payload': ['activity_homework'],
        'hide': True
    },

    'activity_hobby': {
        'title': 'Хобби',
        'payload': ['activity_hobby'],
        'hide': True
    },

    'activity_sport': {
        'title': 'Спорт',
        'payload': ['activity_sport'],
        'hide': True
    },

    'activity_end_yes': {
        'title': 'Завершить активность',
        'payload': ['activity_end'],
        'hide': True
    },
    
    'activity_end_no': {
        'title': 'Отмена',
        'payload': ['activity_continue'],
        'hide': True
    },

    # Statistic
    'statistic': {
        'title': '\U0001F4CA Статистика',
        'payload': ['statistic'],
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


CARDS = {
    'card': {
        'type': 'BigImage',
        'image_id': '937455/659419eb30947371c9e1',
        'title': 'Ваша статистика готова!',
        'button': {
            'text': 'Посмотреть статистику',
            'url': f'{DOMEN}/statistic',
        },
    }
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
    SKILL_BUTTONS['activity_hobby'],
    SKILL_BUTTONS['back']
]

END_ACTIVITY = [
    SKILL_BUTTONS['activity_end_yes'],
    SKILL_BUTTONS['activity_end_no']
]
