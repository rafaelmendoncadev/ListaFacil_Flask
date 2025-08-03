#!/usr/bin/env python3
"""
Railway initialization script
This script runs database migrations and creates initial data if needed
"""

import os
from app import create_app, db
from flask_migrate import upgrade
from app.models import Category

def init_railway():
    """Initialize the application for Railway deployment"""
    app = create_app()
    
    with app.app_context():
        try:
            # Run database migrations
            print("Running database migrations...")
            upgrade()
            
            # Create default categories if they don't exist
            if Category.query.count() == 0:
                print("Creating default categories...")
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
                print(f"Created {len(default_categories)} default categories")
            
            print("Railway initialization completed successfully!")
            
        except Exception as e:
            print(f"Error during Railway initialization: {str(e)}")
            db.session.rollback()
            raise

if __name__ == '__main__':
    init_railway()