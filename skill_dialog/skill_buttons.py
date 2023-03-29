# Кнопки навыка
SKILL_BUTTONS = {
    'dev': {
        'title': 'DEV|Проверяющий: добавить активность длиною в час',
        'payload': ['dev'],
        'hide': False
    },
    'dev_info': {
        'title': 'DEV|Проверяющий: информация для проверяющих',
        'payload': ['dev_info'],
        'hide': False
    },
    'main_menu': {
        'title': 'Главное меню',
        'payload': ['back_to_menu'],
        'hide': True
    },

    # About
    'help': {
        'title': '\U0001F4D6 Помощь',
        'payload': ['help'],
        'hide': True
    },
    'about_skill': {
        'title': 'О навыке',
        'payload': ['about_skill'],
        'hide': True
    },
    'about_activities': {
        'title': 'Об активностях',
        'payload': ['about_activities'],
        'hide': True
    },
    'about_statistic': {
        'title': 'О статистике',
        'payload': ['about_statistic'],
        'hide': True
    },

    'what_you_can': {
        'title': 'Что ты умеешь?',
        'payload': ['what_you_can'],
        'hide': True
    },

    # Activities
    'activities': {
        'title': '\U00002705 Активности',
        'payload': ['activities'],
        'hide': True
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
        'hide': True
    },
    'get_visualisation': {
        'title': 'Визуализация',
        'payload': ['get_visualisation'],
        'hide': False
    },
    'get_entries': {
        'title': 'Список активностей',
        'payload': ['get_entries'],
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

    # Other
    'hello_new_hide': {
        'title': '\U0001F525 Поехали',
        'payload': ['yes'],
        'hide': True
    },
    'back': {
        'title': 'Назад',
        'payload': ['back'],
        'hide': True
    }
}


STATISTIC_ACTIVITIES_CARD = {
    'type': 'ItemsList',
    'header': {
        'text': 'Ваши Активности'
    },
    'items': {

    }
}

WHAT_YOU_CAN_CARD = {
    'type': 'ItemsList',
    'header': {
        'text': ''
    },
    'items': [
        {
            'image_id': '997614/0153ace46ab56d666c5f',
            'title': 'Главное меню',
            'description': 'Перейдите в интересующий вас раздел',
            'button': {
                'payload': ['back_to_menu']
            }
        },
        {
            'image_id': '997614/44b0c878d3ebeea64a34',
            'title': 'Активности',
            'description': 'Здесь вы можете начать или закончить Активность. Хотите узнать больше?',
            'button': {
                'payload': ['about_activities']
            }
        },
        {
            'image_id': '1030494/a386ca38d555d4e1f6d8',
            'title': 'Статистика',
            'description': 'В этом разделе вы сможете взглянуть на результаты своих трудов. '
                           'Рассказать о нём?',
            'button': {
                'payload': ['about_statistic']
            }
        },
        {
            'image_id': '1533899/4b1c74d2a1681bdcf64f',
            'title': 'Навык',
            'description': 'Если хотите узнать больше о навыке, то вам сюда',
            'button': {
                'payload': ['about_skill']
            }
        }
    ],
}

MAIN_MENU_CARD = {
    'type': 'ItemsList',
    'header': {
        'text': ''
    },
    'items': [
        {
            'image_id': '997614/44b0c878d3ebeea64a34',
            'title': 'Активности',
            'description': 'Здесь вы можете начать или закончить Активность',
            'button': {
                'text': 'Активности',
                'payload': ['activities']
            }
        },
        {
            'image_id': '1030494/a386ca38d555d4e1f6d8',
            'title': 'Статистика',
            'description': 'В этом разделе вы сможете взглянуть на результаты своих трудов',
            'button': {
                'text': 'Статистика',
                'payload': ['statistic']
            }
        },
        {
            'image_id': '213044/40740b20816d29f6406b',
            'title': 'Помощь',
            'description': 'Узнайте больше о навыке',
            'button': {
                'text': 'Помощь',
                'payload': ['help']
            }
        }
    ]
}

ACTIVITIES_CARD = {
    'type': 'ItemsList',
    'header': {
        'text': ''
    },
    'items': [
        {
            'image_id': '213044/39799b3319bd0fb5135b',
            'title': 'Работа',
            'description': 'Все мы ждём выходных, а пока трудимся',
            'button': {
                'text': 'Работа',
                'payload': ['activity_work']
            }
        },
        {
            'image_id': '213044/1ad7f49599385016222d',
            'title': 'Домашние Дела',
            'description': 'Иногда нужно уделять время и дому',
            'button': {
                'text': 'Домашние Дела',
                'payload': ['activity_homework']
            }
        },
        {
            'image_id': '213044/b85af62b5e29b538daca',
            'title': 'Хобби',
            'description': 'Кто откажется от любимого занятия?',
            'button': {
                'text': 'Хобби',
                'payload': ['activity_hobby']
            }
        },
        {
            'image_id': '213044/d458652c075b18128692',
            'title': 'Спорт',
            'description': 'Поддерживайте тело в хорошей форме, а '
                           'оно поддержит Вас!',
            'button': {
                'text': 'Спорт',
                'payload': ['activity_sport']
            }
        },
        {
            'image_id': '1030494/edca956f6dd3f17aa057',
            'title': 'Прочее',
            'description': 'Всякая, но не менее важная, всячина',
            'button': {
                'text': 'Прочее',
                'payload': ['activity_other']
            }
        },
    ]
}

ABOUT_SKILL_CARD = {
    'type': 'BigImage',
    'image_id': '1533899/4b1c74d2a1681bdcf64f',
    'title': 'О навыке',
    'description': (
        'Этот навык призван помочь Вам следить за тем, как Вы распределяете своё время. Если Вы активная '
        'личность, дорожащая каждой минутой и желающая оценить свои временные затраты - Контроль Времени '
        'обязательно поможет Вам в этом деле. В разделе "Активности" Вы сможете делать отметки о начале и конце'
        'ваших активностей, а раздел "Статистика" предоставит Вам краткую информацию о Ваших активностях в виде'
        'текста и круговой диаграммы. Скажите, если хотите узнать подробнее о статистике и активностях. Или же '
        'вернёмся в главное меню?'
    )
}

ABOUT_ACTIVITIES_CARD = {
    'type': 'BigImage',
    'image_id': '997614/44b0c878d3ebeea64a34',
    'title': 'Об активностях',
    'description': (
        'Активности представляют собой записи о Ваших действиях в течение дня. Существует несколько видов '
        'Активностей: "Работа", "Домашние Дела", "Хобби", "Спорт", "Прочее". Начав отслеживать ' 
        'Активность, Вы можете добавить произвольный текст к её описанию. Оговоримся, что Активности, ' 
        'на которые Вы тратите мало времени в течение дня, лучше отмечать в разделе "Прочее", '
        'а Активности, продолжительность которых меньше минуты, будут проигнорированы. '
        'Так, Ваша статистика будет составлена точнее, а значит станет полезнее для Вас! Хотите ' 
        'узнать о навыке и статистике? Или же вернёмся в главное меню?'
    )
}

ABOUT_STATISTIC_CARD = {
    'type': 'BigImage',
    'image_id': '1030494/a386ca38d555d4e1f6d8',
    'title': 'О статистике',
    'description': (
        'Наверняка вам захочется посмотреть на результаты ваших трудов, поэтому спешим вас обрадовать: Вы ' 
        'можете узнать свою статистику за сегодняшний и предыдущие дни! Кроме того, что Вы сможете ' 
        'посмотреть на неё в виде текстовых записей, мы добавим визуализацию в виде круговой диаграммы. ' 
        'Хотите узнать о навыке и активностях? Или же вернёмся в главное меню?'
    )
}

STATISTIC_VISUAL_CARD = {
    'type': 'BigImage',
    'image_id': None
}

MAIN_MENU_BUTTONS = [
    SKILL_BUTTONS['activities'],
    SKILL_BUTTONS['statistic'],
    SKILL_BUTTONS['help'],
    SKILL_BUTTONS['what_you_can'],
    SKILL_BUTTONS['dev'],
    SKILL_BUTTONS['dev_info']
]

HELP_BUTTONS = [
    SKILL_BUTTONS['about_skill'],
    SKILL_BUTTONS['about_activities'],
    SKILL_BUTTONS['about_statistic'],
    SKILL_BUTTONS['back']
]

ACTIVITY_TYPES = [
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
    SKILL_BUTTONS['main_menu']
]

POSSIBILITIES_BUTTONS = [
    SKILL_BUTTONS['main_menu'],
    SKILL_BUTTONS['about_activities'],
    SKILL_BUTTONS['about_statistic'],
    SKILL_BUTTONS['about_skill']
]

HELLO_NEW_BUTTONS = [
    SKILL_BUTTONS['hello_new_hide']
]
