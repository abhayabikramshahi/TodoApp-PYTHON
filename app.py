from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Required for flash messages
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Todo Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50))
    due_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'task': self.task,
            'category': self.category,
            'due_date': self.due_date.strftime('%Y-%m-%d') if self.due_date else None,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    category_filter = request.args.get('category', '')
    status_filter = request.args.get('status', '')
    
    query = Todo.query
    
    if category_filter:
        query = query.filter_by(category=category_filter)
    if status_filter:
        query = query.filter_by(status=status_filter)
    
    todos = query.order_by(Todo.created_at.desc()).all()
    categories = db.session.query(Todo.category).distinct().all()
    categories = [cat[0] for cat in categories if cat[0]]
    
    return render_template('index.html', 
                         todos=todos, 
                         categories=categories,
                         current_category=category_filter,
                         current_status=status_filter)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    category = request.form.get('category')
    due_date = request.form.get('due_date')
    
    if not task:
        flash('Task cannot be empty!', 'error')
        return redirect(url_for('index'))
    
    try:
        due_date = datetime.strptime(due_date, '%Y-%m-%d').date() if due_date else None
    except ValueError:
        flash('Invalid date format!', 'error')
        return redirect(url_for('index'))
    
    todo = Todo(
        task=task,
        category=category if category else None,
        due_date=due_date,
        status='Pending'
    )
    
    db.session.add(todo)
    db.session.commit()
    flash('Task added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/update/<int:todo_id>', methods=['POST'])
def update(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    action = request.form.get('action')
    
    if action == 'toggle':
        todo.status = 'Completed' if todo.status == 'Pending' else 'Pending'
    elif action == 'delete':
        db.session.delete(todo)
    
    db.session.commit()
    flash('Task updated successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/filter')
def filter_todos():
    category = request.args.get('category', '')
    status = request.args.get('status', '')
    return redirect(url_for('index', category=category, status=status))

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 