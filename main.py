from flask import Flask, render_template, request, redirect, url_for
from db import db
from models import Atividade

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
db.init_app(app)

@app.route('/')
def home():
    registros = db.session.query(Atividade).all()
    return render_template('index.html', registros=registros)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return render_template('cadastrar_tarefa.html')
    elif request.method == 'POST':
        nome = request.form['nomeForm']
        tarefa = request.form['tarefaForm']
        data = request.form['dataForm']
        
        nova_tarefa = Atividade(nome=nome, tarefa=tarefa, data=data)
        db.session.add(nova_tarefa)
        db.session.commit()
        return redirect(url_for('home'))
    
@app.route('/deletar/<int:id>')
def deletar(id):
    registro = db.session.query(Atividade).filter_by(id=id).first()
    db.session.delete(registro)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)