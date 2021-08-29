from flask import (
    jsonify,
    Blueprint
)
import socket
import logging
from app.url_tokens import *

ronin_blueprint = Blueprint('ronin_url_token_api', __name__)
logconsole = logging.getLogger('console')


@ronin_blueprint.route('/')
@ronin_blueprint.route('/index')
def index():
    host_local_ip = socket.gethostbyname(socket.gethostname())
    response = {"message": "welcome to app file", "local_ip": host_local_ip}
    logconsole.info(response)
    return jsonify(response)


@ronin_blueprint.route('/active_token', methods=['GET'])
def active_token():
    response = {}
    current_token = UrlTokens.find_active_url_token()
    if current_token:
        success = True
        response.update({
            'success': success,
            'token': current_token.token
        })
    else:
        success = False
        response.update({
            'success': success,
            'token': None
        })
    return jsonify(response)
