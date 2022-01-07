# TODO: Implement database schema
from datetime import datetime
from app import db

# TODO: Add group ids, for the navbar board grouping
class Board(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer, primary_key=True)
    boardname = db.Column(db.String(64), unique=True)
    subtitle = db.Column(db.String(64), nullable=True)
    boardpath = db.Column(db.String(5), unique=True)
    hidden = db.Column(db.Boolean)
    ops = db.relationship('OP', backref='board')
    bump_limit = db.Column(db.Integer)
    def __repr__(self):
        return '<Board /{}/>: {} - {}'.format(self.boardpath, self.boardname, self.subtitle)


# TODO: figure out how to handle images on posts
# TODO: Add author ids
class OP(db.Model):
    __tablename__ = 'op'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    posts = db.relationship('Post', backref='op', lazy='dynamic')
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))


quotes = db.Table('quotes',
                  db.Column('quotes_id', db.Integer, db.ForeignKey('post.id')),
                  db.Column('quoted_id', db.Integer, db.ForeignKey('post.id')))

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    op_id = db.Column(db.Integer, db.ForeignKey('op.id'))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    quotes = db.relationship('Post', secondary=quotes,
                             primaryjoin=(quotes.c.quotes_id == id),
                             secondaryjoin=(quotes.c.quoted_id == id),
                             backref=db.backref('quoted', lazy='dynamic'))

    def __repr__(self):
        return '<Post ID: {}> {} on OP >>{}'.format(self.id, self.body, self.op_id)