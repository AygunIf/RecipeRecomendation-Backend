from model import User, db


def get_user_by_token(token):
    user = User.query.filter_by(connection_token = token).first()
    if user is None:
        return {'message': 'User not found.'}, 404
    return user.to_dict(), 200


def create_new_connection():
    new_user = User()
    new_user.create_connection_token()

    db.session.add(new_user)
    db.session.commit()

    return {'message': 'Connection Created', 'connection_token': new_user.connection_token}, 200