from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadstro.bd'

BD = SQLAlchemy(app)


# Define uma Tabela
class Registro(BD.Model):
    id = BD.Column(BD.Integer(), primary_key=True, autoincrement=True)
    nome = BD.Column(BD.String(255), index=True)
    cpf = BD.Column(BD.String(255))
    email = BD.Column(BD.String(255))
    telefone = BD.Column(BD.String(255))

    def __init__(self, nome, cpf, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return '<Nome: {}>'.format(self.nome)


BD.create_all()


@app.route('/')
def home():
    result = "<h1>Tabelas</h1><br><ul>"
    for table in BD.metadata.tables.items():
        result += "<li>%s</li>" % str(table)
    result += "</ul>"
    return result


@app.route('/adc/')
def addRegistro():
    result = "<h1>Adição de Registro</h1><br><ul>"
    login = Registro(nome='Fernando', cpf='405649976-10', email='nando293@gmail.com', telefone='34087922')
    BD.session.add(login)
    BD.session.commit()
    result += "<h4>Cliente Adicionado</h4>"
    return result


@app.route('/deletar/<int:id>')
def delPeople(id):
    result = "<h1>Exclusão de Registro</h1><br><ul>"
    cliente = Registro.query.get(id)
    BD.session.delete(cliente)
    BD.session.commit()
    result += '<p>Cliente -> Id=' + str(cliente.id) + ' Excluido!</p>'
    return result


@app.route('/mostrar/<int:id>')
def showPerson(id):
    people = Registro.query.get(id)
    result = "<h1>Consulta a Registro</h1><br><ul>"
    result += "<p> Id =" + str(people.id) + "</p>"
    result += "<p> Nome =" + people.nome + "</p>"
    result += "<p> CPF =" + people.cpf + "</p>"
    result += "<p> E-mail =" + people.email + "</p>"
    result += "<p> Telefone=" + people.telefone + "</p>"

    return result


@app.route('/listar')
def showPeople():
    people = Registro.query.order_by(Registro.id).all()
    result = '<h1>Cliente</h1><br><ul>'
    for people in people:
        result += '<p>'
        result += 'Id=' + str(people.id)
        result += " <br>Nome = " + people.nome
        result += " <br>CPF = " + people.cpf
        result += " <br>E-mail = " + people.email
        result += " <br>Telefone = " + people.telefone
        result += '</p>'
    return result


@app.route('/alterar/<int:id>')
def alterar(id):
    cliente = Registro.query.get(id)
    cliente.nome = 'Fernando Vinícius Araújo'
    BD.session.commit()
    return 'MUDANÇA CONFIRMADA!'


if __name__ == '__main__':
    app.run()
