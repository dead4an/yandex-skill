# Словарь для классификации запроса (cheap-NLP)
# Работает с токенами из запроса
command_classifier_dict = {
    'start': {
        'поехали', 'начать', 'давай', 'да', 'начинай',
        'начнём', 'старт', 'вперед', 'вперёд', 'начало',
        'дальше', 'ага', 'угу'
    },

    # Главное меню
    'help': {
        'гайд', 'научи', 'инструкция'
        'информация', 'help', 'помощь', 'как', 'пользоваться',
        'использовать', 'навыком', 'мне', 'почему'
    },
    'activities': {
        'отметка',  'отметку', 'отметиться', 'засечь', 'время',
        'сделать', 'запиши', 'записать', 'отслеживать', 'отмечай',
        'отметь', 'засеки', 'добавить', 'отметки', 'активность',
        'активности', 'новая', 'новую', 'добавь', 'activities'
    },
    'statistic': {
        'статистика', 'статистику', 'график', 'диаграмма', 'гистограмма',
        'моя', 'мою', 'посмотреть', 'узнать', 'поделись', 'покажи',
        'показать', 'показывай', 'statistic'
    },
    'what_you_can': {
        'что', 'ты', 'умеешь', 'можешь', 'what_you_can',
        'навыке', 'навык', 'умеет', 'рассказать', 'расскажет'
    },

    # Активности
    'activity_work': {
        'работа', 'работы', 'работу', 'работе',
        'на'
    },
    'activity_hobby': {
        'увлечения', 'хобби', 'интересы'
    },
    'activity_homework': {
        'домашние', 'дом', 'дома', 'дела',
        'по', 'дому', 'в', 'доме'
    },
    'activity_sport': {
        'спорт', 'спортом', 'спортивную',
        'спортивная', 'спорту', 'спортивные',
        'спорте', 'физические', 'упражнения',
    },
    'activity_other': {
        'прочее', 'остальное', 'другое',
        'разное', 'прочая', 'прочую',
        'разности', 'activity_other'
    },

    # Завершение актинвости
    'close_activity': {
        'закончить', 'стоп', 'остановить', 'завершить',
        'конец', 'закончила', 'закончил', 'закончи',
        'да', 'именно', 'ага', 'угу', 'завершай',
        'окончить', 'close_activity'
    },
    'continue_activity': {
        'нет', 'отмена', 'продолжи', 'продолжать',
        'назад', 'продолжай', 'отменить', 'continue_activity',
        'дальше'
    },

    # Статистика
    'get_entries': {
        'записи', 'активности', 'текст', 'активность',
        'отметки', 'get_entries', 'список', 'активностей',
        'подробная', 'подробную'
    },
    'get_daily_statistic': {
        'день', 'сегодня', 'сегодняшняя', 'сегодняшнюю',
        'весь', 'общая', 'get_daily_statistic'
    },
    'get_weekly_statistic': {
        'неделя', 'неделю', 'вся', 'всю',
        'недельная', 'недельную', 'общая',
        'get_weekly_statistic'
    },

    # Статистика | пагинация
    'entries_continue': {
        'далее', 'продолжи', 'продолжать', 'следующая',
        'дальше', 'следующие', 'следующую', 'вперёд', 'вперед',
        'продолжим', 'продолжаем'
    },
    'entries_previous': {
        'назад', 'предыдущая', 'прошлая',
        'до', 'entries_previous',
        'перед', 'предыдущую'
    },

    # Статистика | Неделя
    'one_ago': {
        'вчера', 'один', 'вчерашний', 'вчерашнюю',
        'день', 'вчерашняя'
    },
    'two_ago': {
        'позавчера', 'два', 'позавчерашний', 'позавчерашнюю',
        'позавчерашняя'
    },
    'three_ago': {
        'три', 'позапозавчера'
    },
    'four_ago': {
        'четыре'
    },
    'five_ago': {
        'пять', 'дней'
    },

    # Разделы помощи
    'about_skill': {
        'навык', 'навыке', 'умение', 'общая', 'общих',
        'зачем', 'about_skill', 'навыком', 'навыки'
    },
    'about_activities': {
        'отметки', 'активности', 'отметках', 'активностях',
        'about_activities', 'активностью', 'активность',
        'активный'
    },
    'about_statistic': {
        'статистика', 'статистике', 'результаты', 'итоги',
        'визуализация', 'about_statistic', 'статистику',
        'статистики'
    },
    'repeat': {
        'повтори', 'ещё', 'раз', 'снова', 'заново',
        'повтор', 'повторить', 'повторяй'
    },

    # Подтверждение | отрицание
    'yes': {
        'да', 'ага', 'начать', 'начнём', 'давай', 'вперёд',
        'именно', 'продолжи', 'продолжай', 'угу', 'так',
        'согласен', 'согласна', 'поехали', 'yes', 'начнем',
    },

    'no': {
        'нет', 'не-а', 'не', 'отмени', 'отмена', 'верни',
        'стой', 'стоп', 'подожди', 'потом', 'никак', 'no',
    },

    # Назад | в главное меню
    'back': {
        'вернуться', 'назад', 'отменить', 'отмени', 'верни',
        'отмена', 'предыдущий', 'back'
    },

    'back_to_menu': {
        'главное', 'меню', 'в', 'back_to_menu'
    },

    'quit': {
        'пока', 'закрыть', 'выйти', 'выход'
    }
}

METRICS = {
    # Главное меню
    'main_menu': ['yes', 'no', 'help', 'activities',
                  'statistic', 'what_you_can', 'quit',
                  'start'],

    # Активности
    'activity_types': ['activity_work', 'activity_homework',
                       'activity_hobby', 'activity_sport',
                       'activity_other', 'back', 'statistic',
                       'back_to_menu'],
    'close_activity': ['close_activity', 'continue_activity'],

    # Статистика
    'statistic': ['get_entries', 'get_daily_statistic',
                  'get_weekly_statistic', 'back', 'back_to_menu',
                  'activities'],

    'entries_view': ['entries_continue', 'entries_previous',
                     'no', 'back_to_menu', 'get_daily_statistic'],

    'weekly_view': {
        'one_ago', 'two_ago', 'three_ago',
        'four_ago', 'five_ago', 'back_to_menu',
        'get_daily_statistic', 'get_entries'
    },

    'weekly_view_day': {
        'back', 'back_to_menu'
    },

    'what_you_can': {
        'yes', 'entries_continue', 'no', 'back_to_menu',
        'about_skill', 'activities', 'statistic', 'help'
    },

    'what_you_can_repeat': {
        'yes', 'no', 'repeat', 'back_to_menu',
        'about_skill', 'activities', 'statistic',
        'help'
    },

    # Помощь
    'help': ['about_skill', 'about_activities', 'about_statistic',
             'what_you_can', 'back', 'back_to_menu']
}


def classify_command(tokens: list, metrics: list):
    counter = {key: 0 for key in metrics}
    for metric in metrics:
        for token in tokens:
            if token in command_classifier_dict[metric]:
                counter[metric] += 1

    counter = list(sorted(counter.items(), key=lambda x: x[1]))
    if counter[-1][1]:
        return counter[-1][0]

    return None
