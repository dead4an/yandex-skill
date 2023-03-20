class Response:
    def __init__(self, text: str, buttons=None, card=None,
                 session_state=0, end_session=False) -> None:
        self.text = text
        self.buttons = buttons
        self.card = card
        self.session_state = session_state
        self.end_session = end_session
        self.version = '1.0'

    def respond(self) -> dict:
        """ Подготавливает и возвращает ответ """
        response = {
            'response': {
                'text': self.text,
                'end_session': self.end_session
            },
            'session_state': {
                'value': self.session_state
            },
            'version': self.version
        }

        if self.card:
            response['response'].update({'card': self.card})
        
        if self.buttons and len(self.buttons) > 0:
            response['response'].update({'buttons': self.buttons})

        return response
