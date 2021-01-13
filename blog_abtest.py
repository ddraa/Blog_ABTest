from flask import Flask, jsonify, request, render_template, make_response
from flask_login import login_manager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secure_key = 'static'

login_manager = login_manager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@login_manager.user_unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)