from flask import Blueprint, jsonify, request

from src.models.user_model import User
from src.databases.user_database import *

user = Blueprint(
    'user',
    __name__,
    url_prefix='/api/v1/user'
)


@user.post('/create')
def handle_create():
    if request.is_json:
        body = dict(request.get_json())
        user_data = {
            'email': body.get('email'),
            'password': body.get('password'),
            'username': body.get('username')
        }
        user_data = {k: v for k, v in user_data.items() if v is not None}
        new_user = User(**user_data)
        flag, user_dict = create_user(new_user)
        print('I am here...')
        print(user_dict)
        if flag:
            return jsonify({
                'message': 'SUCCESS',
                'user': user_dict
            }), 201
    else:
        return jsonify({
            'message': 'REQUEST HAS NO BODY'
        }), 400


@user.get('/get/<string:id>')
def handle_get(id: str):
    user = get_user_by_id(id, do_serialize=True)
    if user:
        return jsonify({
            'message': 'SUCCESS',
            'user': user
        }), 200
    else:
        return jsonify({
            'message': f'NO USER FOUND WITH THE ID: {id}'
        }), 400


@user.put('/update/<string:id>')
def handle_update(id: str):
    user = get_user_by_id(id, do_serialize=True)
    if user:
        if request.is_json:
            body = dict(request.get_json())
            user_data = {k: v for k, v in body.items() if v is not None}
            flag, user_dict = update_user_by_id(
                id, user_data, do_serialize=True)
            if flag:
                return jsonify({
                    'message': 'SUCCESS',
                    'user': user_dict
                }), 200
            else:
                return jsonify({
                    'message': 'SERVER ERROR'
                }), 500
        else:
            return jsonify({
                'message': 'BAD REQUEST'
            }), 400
    else:
        return jsonify({
            'message': f'NO USER FOUND WITH THE ID: {id}'
        }), 400


@user.delete('/delete/<string:id>')
def handle_delete(id: str):
    user = get_user_by_id(id, do_serialize=True)
    if user:
        flag, user_dict = update_user_by_id(
            id, {User.is_deleted: True}, do_serialize=True)
        if flag:
            return jsonify({
                'message': 'SUCCESS'
            }), 200
        else:
            return jsonify({
                'message': 'SERVER ERROR'
            }), 500
    else:
        return jsonify({
            'message': f'NO USER FOUND WITH THE ID: {id}'
        }), 400
