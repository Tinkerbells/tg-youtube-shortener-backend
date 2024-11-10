from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'}), 200
