# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/the-beatles', methods=['POST', 'GET'])
def beatles():
    
    
    MUSICA_E_DOS_BEATLES = ''

    def verificar_se_musica_e_dos_beatles(musica):

        MUSICAS_DOS_BEATLES = [
            'in my life', 
            'blackbird',
            'helter skelter',
            'something',

        ]
        print(musica)

        if musica.lower() in MUSICAS_DOS_BEATLES:
            return True
        else:
            return False

    if request.method == 'POST':

        musica = request.form['nome-musica']

        if verificar_se_musica_e_dos_beatles(musica):
            MUSICA_E_DOS_BEATLES = 'Sim, música dos Beatles'
        else:
            MUSICA_E_DOS_BEATLES = 'Não é, =('

    return f'''

        <form action="/the-beatles" method="POST">
            <label for="nome-musica"> Nome da Música</label>
            <input type="text id="nome-musica" name="nome-musica">
            <button>Ver se é música dos Beatles</button>
        </form>

        <p>{MUSICA_E_DOS_BEATLES}</p>

    '''


@app.route('/')
def hello():
    return '''

    <style>

        img {
            width: 500px;
            heigth: 500px;
        }

        .imagem-grande {
            width: 500px;
            heigth: 400px:

        }

        .imagem-pequena {
            width: 250px;
            heigth: 200px;
        }

        #letreiro{
            font-size: 25px;
            color: red;

        }

    </style>
    
    <h1>Flask App</h1>
    <hr>
    <h2> Meu primeiro aplicativo em Flask</h2>

    <p>
        <marquee id="letreiro">The Beatles</marquee>
        <img class="imagem-grande"src="https://as2.ftcdn.net/jpg/00/66/71/53/500_F_66715348_JfbBof8OfR7nYBk7RjHcQIUbDu4MHilQ.jpg">
        <img class="imagem-pequena" src="https://as2.ftcdn.net/jpg/00/34/62/29/500_F_34622954_sdELILidBcNek9XjtIoNAbsYygQXU3NC.jpg">


    </p>
    <p> by: <strong>Arthur Nasser</strong></p>
    '''

if __name__ == "__main__":
    os.environ['FLASK_APP'] = 'app'
    os.environ['FLASK_ENV'] = 'development'
    
    app.run()