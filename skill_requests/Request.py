from skill_dialog.nlu import classify_command, METRICS


class Request:
    def __init__(self, request: dict) -> None:
        self.request = request
        self.user_id = request['session']['user']['user_id']
        self.command = ''
        self.session_is_new = request['session']['new']
        self.session_state = 0
        self.timezone = request['meta']['timezone']

        self.init_session_state()
        self.init_command()

    def init_session_state(self) -> None:
        """ Инициализирует состояние сессии """
        if 'value' not in self.request['state']['session']:
            self.session_state = 1
            return

        self.session_state = self.request['state']['session']['value']

    def init_command(self) -> None:
        """ Инициализирует команду пользователя """
        if self.request['request']['type'] == 'ButtonPressed':
            self.command = self.request['request']['payload'][0]
            return

        nlu_tokens = self.request['request']['nlu']['tokens']
        if self.session_state == 1:
            self.command = classify_command(nlu_tokens, METRICS['main_menu'])

        elif self.session_state == 2:
            self.command = classify_command(nlu_tokens, METRICS['activity_types'])
        
        elif self.session_state == 21 or self.session_state == 22:
            self.command = classify_command(nlu_tokens, METRICS['close_activity'])

        elif self.session_state == 3:
            self.command = classify_command(nlu_tokens, METRICS['statistic'])

        elif self.session_state >= 31:
            self.command = classify_command(nlu_tokens, METRICS['entries_view'])

        elif self.session_state == 4 or self.session_state == 6:
            self.command = classify_command(nlu_tokens, METRICS['help'])

    def get_user_id(self):
        """ Возвращает id пользователя """
        return self.user_id

    def get_command(self) -> str:
        """ Возвращает текст команды пользователя """
        return self.command

    def get_session_info(self) -> int and bool:
        """ Возвращает сведения о состоянии сессии """
        return self.session_state, self.session_is_new

    def get_timezone(self):
        return self.timezone
