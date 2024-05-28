from model import User, Answers, db

## CRUD Operations
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


## Extras
def add_user_answer(token, answer_id):
    
    user = User.query.filter_by(connection_token = token).first()
    answer = Answers.query.filter_by(answer_id = answer_id).first()

    if user is None:
        return {'message': 'User not found.'}, 404

    if answer is None:
        return {'message': 'Answer not found.'}, 404
    
    user.answers.append(answer)

    # save the selected answer in the data base
    db.session.add(answer)
    db.session.commit()

    return {'message': 'Done!'}, 200


