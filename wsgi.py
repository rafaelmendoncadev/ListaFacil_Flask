#!/usr/bin/env python3
"""
WSGI entry point for production deployment
"""

import os
from app import create_app, db
from flask_migrate import upgrade

# Create the Flask application
app = create_app()

# Force database initialization for production
try:
    with app.app_context():
        # Run migrations
        upgrade()
        print("Database migrations completed")
        
        # Ensure categories exist
        from app.models import Category
        if Category.query.count() == 0:
            default_categories = [
                {'name': 'Laticínios & Ovos', 'color': '#FEF3C7'},
                {'name': 'Carnes & Peixes', 'color': '#FEE2E2'},
                {'name': 'Frutas & Vegetais', 'color': '#D1FAE5'},
                {'name': 'Padaria', 'color': '#FED7AA'},
                {'name': 'Bebidas', 'color': '#DBEAFE'},
                {'name': 'Limpeza', 'color': '#E0E7FF'},
                {'name': 'Higiene', 'color': '#F3E8FF'},
                {'name': 'Outros', 'color': '#F3F4F6'}
            ]
            
            for cat_data in default_categories:
                category = Category(name=cat_data['name'], color=cat_data['color'])
                db.session.add(category)
            
            db.session.commit()
            print(f"Created {len(default_categories)} categories")
        
except Exception as e:
    print(f"Database initialization warning: {e}")
    # Continue anyway

if __name__ == "__main__":
    # This is for local testing only
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)