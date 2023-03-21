DOMEN = 'https://40a2-83-220-236-37.eu.ngrok.io'

# Кнопки навыка
SKILL_BUTTONS = {
    # About
    'help': {
        'title': 'Помощь \U0001F4D6',
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

    # Checkin
    'activities': {
        'title': 'Отметки \U00002705',
        'payload': ['activities'],
        'hide': False
    },
    'create_activity': {
        'title': 'Отметиться',
        'payload': ['checkin'],
        'hide': False
    },

    # Statistic
    'statistic': {
        'title': 'Моя статистика \U0001F4CA',
        'payload': ['statistic'],
        'hide': False
    },

    # Hello
    'hello_new': {
        'title': 'Поехали \U0001F525',
        'payload': ['yes'],
        'hide': False
    },

    'back': {
        'title': 'Назад',
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
