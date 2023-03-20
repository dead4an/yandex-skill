from flask import Flask, request, render_template
from skill_requests.Request import Request
from skill_dialog.handler import DialogHandler
import time


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    """ Точка входа в приложение """
    start = time.time()
    # Обработка запроса
    req = Request(request.json)
    user_id = req.get_user_id()
    command = req.get_command()
    session_state, session_is_new = req.get_session_info()
    timezone = req.get_timezone()

    # Подготовка ответа
    dialog = DialogHandler(
        user_id, command, session_state,
        session_is_new, timezone
    )
    dialog.process()
    print('Time: ', time.time() - start)
    return dialog.respond()


@app.route('/statistic', methods=['POST', 'GET'])
def stat():
    return render_template('statistic.html')


app.run('0.0.0.0', port=5000, debug=True)
