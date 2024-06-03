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


def calculate_user_dosha_type(token):

    usr = User.query.filter_by(connection_token=token).first()

    if usr is None:
        return {'message': 'User not found.'}, 404
    
    if len(usr.answers)<15:
        return {'message': 'User dont have answers yet'}, 200

    a_alt = 0
    b_alt = 0
    c_alt = 0

    for a in usr.answers:
        if a.alt_letter == 'a':
            a_alt+=1
        if a.alt_letter == 'b':
            b_alt+=1
        if a.alt_letter =='c':
            c_alt+=1

    if a_alt > b_alt and a_alt>c_alt:
        usr.dosha_type = 'Vata'
    if b_alt > a_alt and b_alt>c_alt:
        usr.dosha_type = 'Pitta'
    if c_alt > a_alt and c_alt>b_alt:
        usr.dosha_type = 'Kapha'

    db.session.add(usr)
    db.session.commit()

    return {'message': 'Dosha type calculated', 'dosha_type': usr.dosha_type}, 200

