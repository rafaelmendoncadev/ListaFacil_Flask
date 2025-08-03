# ListaFácil - Shopping List SAAS

A modern, responsive shopping list management system built with Flask and SQLite. Perfect for personal use or as a starting point for a micro SAAS application.

## Features

- 🛒 **Multiple Shopping Lists**: Create and manage multiple lists for different occasions
- 🏷️ **Category Management**: Organize items with customizable categories and colors
- 💰 **Price Tracking**: Add estimated prices and track your shopping budget
- ✅ **Progress Tracking**: Visual progress bars and completion statistics
- 🌙 **Dark Mode**: Toggle between light and dark themes
- 📱 **Mobile Responsive**: Works perfectly on all device sizes
- 👤 **User Authentication**: Secure login and registration system
- 📊 **Purchase History**: Track your shopping patterns over time

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Tailwind CSS (via CDN)
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF with CSRF protection

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ListaFacil
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your browser** and navigate to `http://localhost:5000`

## Usage

### Getting Started

1. **Register** a new account or **login** with existing credentials
2. **Create your first shopping list** from the dashboard
3. **Add items** to your list with categories, quantities, and estimated prices
4. **Check off items** as you shop to track your progress
5. **Manage categories** to organize your items effectively

### Key Features

- **Dashboard**: Overview of all your lists with progress indicators
- **List Management**: Create, edit, archive, and delete shopping lists
- **Item Management**: Add, edit, delete, and mark items as purchased
- **Categories**: Create custom categories with color coding
- **Progress Tracking**: Visual progress bars showing completion status
- **Price Estimation**: Track estimated costs for budget planning

## Project Structure

```
ListaFacil/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models
│   ├── forms.py             # WTForms forms
│   ├── auth/                # Authentication blueprint
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── main/                # Main application blueprint
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── templates/           # Jinja2 templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── dashboard.html
│   │   ├── list_detail.html
│   │   ├── create_list.html
│   │   ├── categories.html
│   │   └── auth/
│   └── static/              # Static files
│       ├── js/
│       ├── css/
│       └── images/
├── instance/                # Instance folder for database
├── app.py                   # Application entry point
├── config.py                # Configuration settings
├── init_db.py              # Database initialization script
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Database Schema

- **Users**: User accounts with authentication
- **Lists**: Shopping lists belonging to users
- **Items**: Individual items within lists
- **Categories**: Item categories with color coding
- **PurchaseHistory**: Historical data of purchased items

## Security Features

- Password hashing with Werkzeug
- CSRF protection on all forms
- Input validation and sanitization
- Secure session management
- SQL injection prevention through SQLAlchemy ORM

## Development

### Adding New Features

1. Create database models in `app/models.py`
2. Add forms in `app/forms.py`
3. Create routes in appropriate blueprint
4. Design templates in `app/templates/`
5. Add styling and JavaScript as needed

### Testing

The application includes basic error handling and validation. For production use, consider adding:

- Unit tests
- Integration tests
- Load testing
- Security testing

## Deployment

For production deployment:

1. Set environment variables for security
2. Use a production WSGI server (Gunicorn, uWSGI)
3. Configure a reverse proxy (Nginx)
4. Use a production database (PostgreSQL, MySQL)
5. Enable HTTPS
6. Set up monitoring and logging

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please create an issue in the repository or contact the development team.

---

**ListaFácil** - Making shopping lists simple and organized! 🛒✨