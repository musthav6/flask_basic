from flask import Flask
from routes.api import api_bp
from routes.admin_client import admin_bp
from config import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'your  bd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'my_secret_key'

db.init_app(app)

app.register_blueprint(api_bp, url_prefix='/api/v1')
app.register_blueprint(admin_bp, url_prefix='/admin')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
