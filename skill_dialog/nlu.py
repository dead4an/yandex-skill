# Словарь для классификации запроса (cheap-NLP)
# Работает с токенами из запроса
command_classifier_dict = {
    'about': {
        'навык', 'навыке', 'о', 'расскажи', 'гайд', 'научи', 'инструкция'
        'информация', 'help', 'помощь', 'как', 'пользоваться',
        'использовать', 'навыком', 'мне', 'почему', 'не'
    },
    'checkin': {
        'отметка',  'отметку', 'отметиться', 'засечь', 'время',
        'сделать', 'начать', 'запиши', 'записать',
        'отмечай', 'отметь', 'засеки', 'добавить', 'отметки'
    },
    'statistic': {
        'статистика', 'статистику', 'график', 'диаграмма', 'гистограмма',
        'моя', 'мою', 'посмотреть', 'узнать', 'поделись', 'покажи',
        'показать', 'показывай'
    }
}


def classify_command(tokens: list) -> str:
    counter = {
        'about': 0, 'checkin': 0, 'statistic': 0
    }

    for token in tokens:
        if token in command_classifier_dict['about']:
            counter['about'] += 1
            continue

        if token in command_classifier_dict['checkin']:
            counter['checkin'] += 1
            continue

        if token in command_classifier_dict['statistic']:
            counter['statistic'] += 1

    counted = list(sorted(counter.items(), key=lambda x: x[1]))
    if counted[-1][1] == 0:
        return 'none'

    return counted[-1][0]
