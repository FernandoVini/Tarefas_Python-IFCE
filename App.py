from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello():
    return 'Alô Mundo ! Aqui é o Fernando testando o Flask !'

if __name__ == '__main__':
    app.run()