import os
from app import create_app, db
from app.models import User, List, Item, Category

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'List': List, 'Item': Item, 'Category': Category}

if __name__ == '__main__':
    # Use environment variable for debug mode
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)