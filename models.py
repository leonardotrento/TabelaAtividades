from db import db

class Atividade(db.Model):
    __tablename__ = 'atividades'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    tarefa = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<{self.nome} : {self.tarefa}>'