from flask import render_template
from app import app
from app.forms import PostForm
from app.models import Board

imageboard_name = 'tchan'       #placeholder
boardtitle = '/b/ - Random'     #placeholder
subtitle = 'sickness.'          #placeholder

@app.route('/')
@app.route('/index')
def index():
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
    return render_template('index.html', imageboard_name=imageboard_name, news=news)

@app.route('/<boardpath>', strict_slashes=False, methods=['GET', 'POST'])
def board(boardpath):
    form = PostForm()
    board = Board.query.filter_by(boardpath=boardpath).first_or_404()
    posts = [
        {'id': 1, 'body': 'carai doidokkkkkkkkkkkkk'}
    ]
    return render_template('board.html', imageboard_name=imageboard_name, boardtitle=boardtitle, subtitle=subtitle, form=form, boardpath=boardpath)
