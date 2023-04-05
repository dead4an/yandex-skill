# Кнопки навыка
SKILL_BUTTONS = {
    'main_menu': {
        'title': 'Главное меню',
        'hide': True
    },
    'quit': {
        'title': 'Выйти',
        'hide': True
    },

    # About
    'help': {
        'title': 'Помощь',
        'hide': True
    },
    'about_skill': {
        'title': 'О навыке',
        'hide': True
    },
    'about_activities': {
        'title': 'Об активностях',
        'hide': True
    },
    'about_statistic': {
        'title': 'О статистике',
        'hide': True
    },

    # What you can
    'what_you_can': {
        'title': 'Что ты умеешь?',
        'hide': True
    },

    'what_you_can_continue': {
        'title': 'Продолжи',
        'hide': True
    },

    'what_you_can_repeat': {
        'title': 'Повтори',
        'hide': True
    },

    # Activities
    'activities': {
        'title': 'Активности',
        'hide': True
    },
    'activity_work': {
        'title': 'Работа',
        'hide': True
    },
    'activity_homework': {
        'title': 'Домашние Дела',
        'hide': True
    },

    'activity_hobby': {
        'title': 'Хобби',
        'hide': True
    },
    'activity_sport': {
        'title': 'Спорт',
        'hide': True
    },
    'activity_other': {
        'title': 'Прочее',
        'hide': True
    },
    'activity_end_yes': {
        'title': '\U00002705 Завершить активность',
        'hide': False
    },
    'activity_end_no': {
        'title': '\U0000274C Отмена',
        'hide': False
    },
    'activity_end_yes_hide': {
        'title': 'Завершить активность',
        'hide': True
    },
    
    'activity_end_no_hide': {
        'title': 'Отмена',
        'hide': True
    },
    # Statistic
    'statistic': {
        'title': 'Статистика',
        'hide': True
    },
    'get_entries': {
        'title': 'Подробная статистика',
        'hide': True
    },
    'get_daily_statistic': {
        'title': 'Сегодня',
        'hide': True
    },
    'get_weekly_statistic': {
        'title': 'Неделя',
        'hide': True
    },

    # Statistic pagination
    'entries_continue': {
        'title': 'Следующая страница',
        'hide': True
    },
    'entries_previous': {
        'title': 'Предыдущая страница',
        'hide': True
    },
    'entries_stop': {
        'title': 'Главное меню',
        'hide': True
    },

    # Other
    'hello_new_hide': {
        'title': 'Поехали',
        'hide': True
    },
    'back': {
        'title': 'Назад',
        'hide': True
    }
}


STATISTIC_ACTIVITIES_CARD = {
    'type': 'ItemsList',
    'header': {
        'text': 'Ваши Активности'
    },
    'items': [

    ]
}

DAILY_STATISTIC_CARD = {
    'type': 'ItemsList',
    'header': {
        'text': 'Ваша статистика за день'
    },
    'items': [

    ]
}

WHAT_YOU_CAN_CARD = {
    'type': 'ItemsList',
    'header': {
        'text': ''
    },
    'items': [
        {
            'image_id': '997614/44b0c878d3ebeea64a34',
            'title': 'Отслеживайте свои активности',
            'description': 'Попросите меня начать отслеживать активность, назовите вид активности, '
                           'а всё остальное сделаю я. Как только Вы закончите свои дела - просто '
                           'попросите меня закончить активность и я добавлю запись о ней в вашу '
                           'статистику.',
            'button': {
                'text': 'Активности'
            }
        },
        {
            'image_id': '1030494/a386ca38d555d4e1f6d8',
            'title': 'Узнайте свою статистику',
            'description': 'Как только у вас появится первая запись об активности, Вы сможете '
                           'посмотреть информацию о ней в разделе "Статистика". В этом же разделе '
                           'Вы сможете узнать свою статистику за последнюю неделю.',
            'button': {
                'text': 'Статистика'
            }
        },
        {
            'image_id': '1533899/4b1c74d2a1681bdcf64f',
            'title': 'Помощь',
            'description': 'В разделе помощи я подробно расскажу Вам о том, как пользоваться навыком '
                           'и приведу примеры команд, которыми Вы можете пользоваться. Нажмите, чтобы '
                           'перейти в раздел помощи.',
            'button': {
                'title': 'Помощь'
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
            'description': 'Здесь Вы можете начать или закончить отслеживать активность',
            'button': {
                'text': 'Активности'
            }
        },
        {
            'image_id': '1030494/a386ca38d555d4e1f6d8',
            'title': 'Статистика',
            'description': 'В этом разделе Вы сможете взглянуть на результаты своих трудов',
            'button': {
                'text': 'Статистика'
            }
        },
        {
            'image_id': '213044/40740b20816d29f6406b',
            'title': 'Помощь',
            'description': 'Узнайте больше о навыке',
            'button': {
                'text': 'Помощь'
            }
        }
    ],
    'footer': {

    }
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
                'text': 'Работа'
            }
        },
        {
            'image_id': '213044/1ad7f49599385016222d',
            'title': 'Домашние Дела',
            'description': 'Иногда нужно уделять время и дому',
            'button': {
                'text': 'Домашние Дела'
            }
        },
        {
            'image_id': '213044/b85af62b5e29b538daca',
            'title': 'Хобби',
            'description': 'Кто откажется от любимого занятия?',
            'button': {
                'text': 'Хобби'
            }
        },
        {
            'image_id': '213044/d458652c075b18128692',
            'title': 'Спорт',
            'description': 'Поддерживайте тело в хорошей форме, а '
                           'оно поддержит Вас!',
            'button': {
                'text': 'Спорт'
            }
        },
        {
            'image_id': '1030494/edca956f6dd3f17aa057',
            'title': 'Прочее',
            'description': 'Всякая, но не менее важная, всячина',
            'button': {
                'text': 'Прочее'
            }
        },
    ]
}

STATISTIC_CARD = {
    'type': 'ItemsList',
    'header': {
        'text': 'Статистику за какой период Вы хотели бы увидеть?'
    },
    'items': [
        {
            'image_id': '965417/05e3ab02e94af22568a3',
            'title': 'Подробная статистика',
            'description': 'Здесь Вы можете посмотреть на записи о сегодняшних активностях',
            'button': {
                'text': 'Подробная статистика'
            }
        },
        {
            'image_id': '1533899/30d9e7b5109319d8063c',
            'title': 'Статистика за сегодня',
            'description': 'Здесь Вы можете узнать общую статистику за сегодня',
            'button': {
                'text': 'Статистика за сегодня'
            }
        },
        {
            'image_id': '937455/d2b0b48b30926b65abdc',
            'title': 'Статистика за неделю',
            'description': 'Здесь Вы можете узнать общую статистику за последнюю неделю',
            'button': {
                'text': 'Статистика за неделю'
            }
        }
    ]
}

WEEKLY_STATISTIC_CARD = {
    'type': 'ItemsList',
    'header': {
        'text': 'Статистику за какой день Вы хотели бы посмотреть?'
    }
}

ABOUT_SKILL_CARD = {
    'type': 'BigImage',
    'image_id': '997614/7a322d2769472fb4517f',
    'title': 'О навыке',
    'description': (
        'Этот навык призван помочь Вам следить за тем, как Вы распределяете своё время. Если Вы активная '
        'личность, дорожащая каждой минутой и желающая оценить свои временные затраты - Контроль Времени '
        'обязательно поможет Вам в этом деле. В разделе "Активности" Вы сможете делать отметки о начале и конце '
        'ваших активностей, а раздел "Статистика" предоставит Вам краткую информацию о Ваших активностях в виде '
        'записей. Скажите, если хотите узнать подробнее о статистике и активностях. Или же '
        'вернёмся в главное меню?'
    )
}

ABOUT_ACTIVITIES_CARD = {
    'type': 'BigImage',
    'image_id': '997614/0562f24a7fce15d3fa10',
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
    'image_id': '1521359/d13bed8584ac6a6103ee',
    'title': 'О статистике',
    'description': (
        'Наверняка вам захочется посмотреть на результаты ваших трудов, поэтому спешим вас обрадовать: Вы ' 
        'можете узнать свою статистику за сегодняшний и предыдущие дни! Если Вы хотите узнать подробную '
        'статистику за сегодняшний день, то скажите "Подробная статистика". Общая статистика за день и '
        'за неделю доступна с помощью команд "Статистика за день" и "Статистика за неделю". ' 
        'Хотите узнать о навыке и активностях? Или же вернёмся в главное меню?'
    )
}

HELP_CARD = {
    'type': 'ItemsList',
    'header': {
        'text': 'Вот инструкция по использованию навыка'
    },
    'items': [
        {
            'image_id': '1030494/ef76cc359fe02ddf9efb',
            'title': 'Начало активности',
            'description': (
                'Чтобы начать отслеживать активность, скажите: "Начать активность". '
                'В разделе активностей Вам будет предложено выбрать вид активности, которую Вы '
                'хотите начать отслеживать. Навык запомнит время начала активности, а также её вид.'
            )
        },
        {
            'image_id': '965417/74d4f56a9ce904a206eb',
            'title': 'Завершение активности',
            'description': (
                'Чтобы закончить активность, скажите: "Закончить активность". '
                'Вы увидите информацию об активности с просьбой подтвердить '
                'завершение активности. Чтобы завершить, скажите: "Завершить". '
                'Чтобы отменить завершение, скажите: "Отменить".'
            )
        },
        {
            'image_id': '1030494/2b850cdd7d98cc1284be',
            'title': 'Просмотр статистики за сегодня',
            'description': (
                'Чтобы узнать свою статистику, скажите: "Статистика". Чтобы увидеть '
                'записи о всех активностях, в разделе статистики скажите "Подробная статистика". '
                'Для получения общей статистики за этот день, скажите: "Сегодня".'
            )
        },
        {
            'image_id': '1652229/244c078ca09c64900c2b',
            'title': 'Просмотр статистики за неделю',
            'description': (
                'Чтобы узнать свою статистику за предыдущие дни, перейдите в раздел статистики, '
                'сказав: "Статистика". Далее скажите: "Статистика за неделю" и выберите день, '
                'статистику за который Вы хотите узнать.'
            )
        }
    ]
}

MAIN_MENU_BUTTONS = [
    SKILL_BUTTONS['activities'],
    SKILL_BUTTONS['statistic'],
    SKILL_BUTTONS['help'],
    SKILL_BUTTONS['what_you_can'],
    SKILL_BUTTONS['quit']
]

HELP_BUTTONS = [
    SKILL_BUTTONS['main_menu'],
    SKILL_BUTTONS['what_you_can_continue'],
    SKILL_BUTTONS['what_you_can']
]

HELP_BUTTONS_END = [
    SKILL_BUTTONS['main_menu'],
    SKILL_BUTTONS['what_you_can_repeat'],
    SKILL_BUTTONS['what_you_can']
]

HELP_ABOUT_SKILL = [
    SKILL_BUTTONS['about_activities'],
    SKILL_BUTTONS['about_statistic'],
    SKILL_BUTTONS['main_menu']
]

HELP_ABOUT_ACTIVITIES = [
    SKILL_BUTTONS['about_skill'],
    SKILL_BUTTONS['about_statistic'],
    SKILL_BUTTONS['main_menu']
]

HELP_ABOUT_STATISTIC = [
    SKILL_BUTTONS['about_skill'],
    SKILL_BUTTONS['about_activities'],
    SKILL_BUTTONS['back']
]

ACTIVITY_TYPES = [
    SKILL_BUTTONS['activity_work'],
    SKILL_BUTTONS['activity_homework'],
    SKILL_BUTTONS['activity_hobby'],
    SKILL_BUTTONS['activity_sport'],
    SKILL_BUTTONS['main_menu']
]

END_ACTIVITY = [
    SKILL_BUTTONS['activity_end_yes'],
    SKILL_BUTTONS['activity_end_no'],
    SKILL_BUTTONS['activity_end_yes_hide'],
    SKILL_BUTTONS['activity_end_no_hide']
]

STATISTIC_BUTTONS = [
    SKILL_BUTTONS['get_entries'],
    SKILL_BUTTONS['get_daily_statistic'],
    SKILL_BUTTONS['get_weekly_statistic'],
    SKILL_BUTTONS['main_menu']
]

STATISTIC_BUTTONS_ENTRIES = [
    SKILL_BUTTONS['get_daily_statistic'],
    SKILL_BUTTONS['get_weekly_statistic'],
    SKILL_BUTTONS['main_menu']
]

STATISTIC_BUTTONS_DAILY = [
    SKILL_BUTTONS['get_entries'],
    SKILL_BUTTONS['get_weekly_statistic'],
    SKILL_BUTTONS['main_menu']
]

STATISTIC_BUTTONS_WEEKLY = [
    SKILL_BUTTONS['back'],
    SKILL_BUTTONS['main_menu']
]

WEEKLY_VIEW_BUTTONS = [
    SKILL_BUTTONS['get_entries'],
    SKILL_BUTTONS['get_daily_statistic'],
    SKILL_BUTTONS['main_menu']
]

ENTRIES_BUTTONS_START = [
    SKILL_BUTTONS['entries_continue'],
    SKILL_BUTTONS['get_daily_statistic'],
    SKILL_BUTTONS['get_weekly_statistic'],
    SKILL_BUTTONS['main_menu']
]

ENTRIES_BUTTONS = [
    SKILL_BUTTONS['entries_continue'],
    SKILL_BUTTONS['entries_previous'],
    SKILL_BUTTONS['get_daily_statistic'],
    SKILL_BUTTONS['get_weekly_statistic'],
    SKILL_BUTTONS['main_menu']
]

ENTRIES_BUTTONS_END = [
    SKILL_BUTTONS['entries_previous'],
    SKILL_BUTTONS['entries_stop'],
    SKILL_BUTTONS['get_daily_statistic'],
    SKILL_BUTTONS['get_weekly_statistic'],
    SKILL_BUTTONS['main_menu']
]

ENTRIES_ONLY_ONE_PAGE = [
    SKILL_BUTTONS['get_daily_statistic'],
    SKILL_BUTTONS['get_weekly_statistic'],
    SKILL_BUTTONS['back'],
    SKILL_BUTTONS['main_menu']
]

POSSIBILITIES_BUTTONS = [
    SKILL_BUTTONS['main_menu'],
    SKILL_BUTTONS['what_you_can_continue'],
    SKILL_BUTTONS['help'],
    SKILL_BUTTONS['activities'],
    SKILL_BUTTONS['statistic']
]

POSSIBILITIES_BUTTONS_STATISTIC = [
    SKILL_BUTTONS['main_menu'],
    SKILL_BUTTONS['what_you_can_repeat'],
    SKILL_BUTTONS['help'],
    SKILL_BUTTONS['activities'],
    SKILL_BUTTONS['statistic']
]

HELLO_NEW_BUTTONS = [
    SKILL_BUTTONS['hello_new_hide']
]
