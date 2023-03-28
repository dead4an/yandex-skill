# Словарь для классификации запроса (cheap-NLP)
# Работает с токенами из запроса
command_classifier_dict = {
    # Главное меню
    'dev': {
        'разработчик', 'разработчика', 'dev'
    },
    'dev_info': {
        'проверяющих', 'dev_info'
    },
    'help': {
        'навык', 'навыке', 'о', 'расскажи', 'гайд', 'научи', 'инструкция'
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
        'что', 'ты', 'умеешь', 'можешь', 'what_you_can'
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
        'отметки', 'get_entries', 'список', 'активностей'
    },

    'get_visualisation': {
        'визуализация', 'диаграмма', 'круговая',
        'красивая', 'круг', 'визуализацию', 'диаграмму',
        'get_visualisation'
    },

    'entries_continue': {
        'далее', 'продолжи', 'продолжать', 'следующая',
        'дальше', 'следующие', 'следующую', 'вперёд', 'вперед'
    },

    'entries_previous': {
        'назад', 'предыдущая', 'прошлая',
        'до', 'entries_previous', 'вернуться',
        'перед', 'предыдущую'
    },

    'entries_stop': {
        'entries_stop'
    },

    # Подразделы помощи
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

    # Подтверждение
    'yes': {
        'да', 'ага', 'начать', 'начнём', 'давай', 'вперёд',
        'именно', 'продолжи', 'продолжай', 'угу', 'так',
        'согласен', 'согласна', 'поехали', 'yes', 'начнем',
    },
    'no': {
        'нет', 'не-а', 'не', 'отмени', 'отмена', 'верни',
        'стой', 'стоп', 'подожди', 'потом', 'никак', 'no',
    },

    # Назад
    'back': {
        'вернуться', 'назад', 'отменить', 'отмени', 'верни',
        'отмена', 'предыдущий', 'back'
    },

    'back_to_menu': {
        'главное', 'меню', 'в', 'back_to_menu'
    }
}

METRICS = {
    # Главное меню
    'main_menu': ['yes', 'no', 'help', 'activities',
                  'statistic', 'what_you_can', 'dev',
                  'dev_info'],

    # Активности
    'activity_types': ['activity_work', 'activity_homework',
                       'activity_hobby', 'activity_sport', 'back'],
    'close_activity': ['close_activity', 'continue_activity'],

    # Статистика
    'statistic': ['get_entries', 'get_visualisation',
                  'back', 'back_to_menu'],
    'entries_view': ['entries_continue', 'entries_previous',
                     'entries_stop', 'no', 'back_to_menu'],

    # Помощь
    'help': ['about_skill', 'about_activities',
             'about_statistic', 'back', 'back_to_menu']
}


def classify_command(tokens: list, metrics: list):
    print('METRICS\n', metrics)
    print(tokens)
    counter = {key: 0 for key in metrics}
    for metric in metrics:
        for token in tokens:
            if token in command_classifier_dict[metric]:
                counter[metric] += 1

    counter = list(sorted(counter.items(), key=lambda x: x[1]))
    if counter[-1][1]:
        return counter[-1][0]

    return 'none'
