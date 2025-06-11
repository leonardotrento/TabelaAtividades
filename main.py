from flask import Flask
from db import db
from models import Atividade

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
db.init_app(app)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)