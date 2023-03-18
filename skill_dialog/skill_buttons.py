# Кнопки навыка
SKILL_BUTTONS = {
    # About
    'about': {
        'title': 'Помощь \U0001F4D6',
        'payload': ['about'],
        'hide': False
    },
    'info': {
        'title': 'О навыке',
        'payload': ['info'],
        'hide': False
    },
    'how_checkin': {
        'title': 'Об отметках',
        'payload': ['how_checkin'],
        'hide': False
    },
    'how_statistic': {
        'title': 'О статистике',
        'payload': ['how_statistic'],
        'hide': False
    },

    # Checkin
    'checkin': {
        'title': 'Отметки \U00002705',
        'payload': ['checkin'],
        'hide': False
    },
    'create_checkin': {
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

    # Other
    'hello_new': {
        'title': 'Поехали \U0001F525',
        'payload': ['поехали'],
        'hide': False
    },
    'hello': {
        'title': 'C возвращением! Что займёмся в этот раз?',
        'payload': ['поехали'],
        'hide': False
    }
}

MAIN_MENU_BUTTONS = [
    SKILL_BUTTONS['about'],
    SKILL_BUTTONS['checkin'],
    SKILL_BUTTONS['statistic']
]

ABOUT_BUTTONS = [
    
]

HELLO_BUTTONS = {
    'hello_new': [SKILL_BUTTONS['hello_new']],
    'hello': [SKILL_BUTTONS['hello']]
}
