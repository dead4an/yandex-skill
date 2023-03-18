from flask import Flask, request
from skill_requests.Request import Request
from skill_dialog.handler import DialogHandler


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    """ Точка входа в приложение """
    # Обработка запроса
    req = Request(request.json)
    user_id = req.get_user_id()
    command = req.get_command()
    session_state, session_is_new = req.get_session_info()
    timezone = req.get_timezone()

    print(request.json)

    # Подготовка ответа
    dialog = DialogHandler(
        user_id, command, session_state,
        session_is_new, timezone
    )
    dialog.process()
    return dialog.respond()


app.run('0.0.0.0', port=5000, debug=True)
