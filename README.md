# Flask Todo App

A modern, responsive Todo application built with Flask and Bootstrap 5. This application allows users to manage their tasks with features like categories, due dates, and status tracking.

## Features

- ✨ Clean and modern user interface
- 📱 Fully responsive design
- 📝 Create, read, update, and delete tasks
- 🏷️ Categorize tasks (Work, Personal, Shopping, Health, Other)
- 📅 Set due dates for tasks
- ✅ Mark tasks as complete/incomplete
- 🔍 Filter tasks by category and status
- 💾 Persistent storage using SQLite database
- ⚡ Real-time feedback with flash messages

## Screenshots

![Todo App Screenshot](screenshots/screanshot.png)

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/flask-todo-app.git
cd flask-todo-app
```

2. Create a virtual environment (recommended):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
flask-todo-app/
├── app.py              # Main application file
├── todo.db            # SQLite database file
├── requirements.txt   # Python dependencies
├── README.md         # Project documentation
└── templates/        # HTML templates
    └── index.html    # Main template file
```

## Features in Detail

### Task Management
- Add new tasks with descriptions
- Assign categories to tasks
- Set due dates
- Mark tasks as complete/incomplete
- Delete tasks with confirmation

### Filtering
- Filter tasks by category
- Filter tasks by status (Pending/Completed)
- Clear all filters

### User Interface
- Responsive design that works on all devices
- Clean and intuitive layout
- Visual feedback for all actions
- Confirmation dialogs for destructive actions
- Auto-hiding notifications

## Database Schema

The application uses SQLite with the following schema:

```sql
CREATE TABLE todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    category TEXT,
    due_date DATE,
    status TEXT DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [Bootstrap](https://getbootstrap.com/) - The CSS framework used
- [Bootstrap Icons](https://icons.getbootstrap.com/) - The icon library used
- [SQLAlchemy](https://www.sqlalchemy.org/) - The ORM used

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/yourusername/flask-todo-app](https://github.com/yourusername/flask-todo-app)
