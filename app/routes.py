from flask import Blueprint, request, jsonify
from .models import Task, db
from .auth import register_user, login_user, get_current_user
from flask_jwt_extended import jwt_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/register', methods=['POST'])
def register():
    return register_user()

@main_bp.route('/login', methods=['POST'])
def login():
    return login_user()

@main_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    user = get_current_user()
    tasks = Task.query.filter_by(user_id=user.id).all()
    return jsonify([task.to_dict() for task in tasks]), 200

@main_bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    user = get_current_user()
    data = request.json
    new_task = Task(
        title=data['title'],
        description=data.get('description'),
        priority=data.get('priority', "Low"),
        due_date=data.get('due_date'),
        user_id=user.id
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

@main_bp.route('/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    user = get_current_user()
    task = Task.query.filter_by(id=task_id, user_id=user.id).first_or_404()
    data = request.json
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.priority = data.get('priority', task.priority)
    task.due_date = data.get('due_date', task.due_date)
    task.completed = data.get('completed', task.completed)
    db.session.commit()
    return jsonify(task.to_dict()), 200

@main_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    user = get_current_user()
    task = Task.query.filter_by(id=task_id, user_id=user.id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"}), 200
