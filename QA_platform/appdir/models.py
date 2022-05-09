from appdir import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    original_password = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    invitation_code = db.Column(db.String(32))
    status = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def __str__(self):
        return "id={}, username={}, email={}, original_password={}, password_hash={}, invitation_code={}".format(
            self.id, self.username, self.email, self.original_password, self.password_hash, self.invitation_code
        )


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    description = db.Column(db.String(300), index=True)
    datetime = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Question {}>'.format(self.title)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), index=True)
    datetime = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))


class Viewpoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agree = db.Column(db.Boolean)
    disagree = db.Column(db.Boolean)
    like = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'))


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'))


class Follow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Invite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inviter_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    invitee_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))


class InvitationCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invitation_code = db.Column(db.String(32), index=True)
    create_time = db.Column(db.DateTime)
    is_valid = db.Column(db.Integer)

    def __str__(self):
        return "id={}, invitation_code={}, create_time={}, is_valid={}".format(
            self.id, self.invitation_code, self.create_time, self.is_valid
        )