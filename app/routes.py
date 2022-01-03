from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    imageboard_name = 'tchan'
    news = [
        {
            'title': 'testando massa!',
            'body': 'lorem ipsum dolor sit amet'
        },
        {
            'title': 'quem tá lendo é corno',
            'body': 'você também.'
        }
    ]
    return render_template('index.html', board='/b/', imageboard_name=imageboard_name, news=news)