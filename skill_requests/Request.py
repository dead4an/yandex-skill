from skill_dialog.nlu import classify_command


class Request:
    def __init__(self, request: dict) -> None:
        self.request = request
        self.user_id = request['session']['user']['user_id']
        self.command = ''
        self.new = request['session']['new']
        self.session_state = 0
        self.timezone = request['meta']['timezone']

        self.init_session_state()
        self.init_command()

    def init_session_state(self) -> None:
        """ Инициализирует состояние сессии """
        if 'value' not in self.request['state']['session']:
            self.session_state = 0
            return

        self.session_state = self.request['state']['session']['value']

    def init_command(self) -> None:
        """ Инициализирует команду пользователя """
        if self.request['request']['type'] == 'ButtonPressed':
            self.command = self.request['request']['payload'][0]
            return

        nlu_tokens = self.request['request']['nlu']['tokens']
        self.command = classify_command(nlu_tokens)

    def get_user_id(self):
        """ Возвращает id пользователя """
        return self.user_id

    def get_command(self) -> str:
        """ Возвращает текст команды пользователя """
        return self.command

    def get_session_info(self) -> int and bool:
        """ Возвращает сведения о состоянии сессии """
        return self.session_state, self.new

    def get_timezone(self):
        return self.timezone
