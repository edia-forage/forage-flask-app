from app import app, db
from app.models import User
from flask import jsonify, request


def get_users():
    result = User.query.all()
    if len(result) == 0:
        return "Sorry !! there is nothing to show"
    else:
        return jsonify(result)


def add_user(user_request):
    new_user = User(id=user_request.get('id'), first_name=user_request.get('first_name'),
                    last_name=user_request.get('last_name', ' '), username=user_request.get('username', ' '),
                    company=user_request.get('company', ' '), contact_no=user_request.get('contact_no', ' '),
                    email=user_request.get('email', ' '))
    db.session.add(new_user)
    db.session.commit()


@app.route('/', methods=['POST', 'GET'])
def userapp():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        add_user(request.get_json())
        return 'User added'

    return get_users()
