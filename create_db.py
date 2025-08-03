import os
import sqlite3
from app import create_app, db
from app.models import User, List, Item, Category, PurchaseHistory

def create_database():
    """Create database and tables."""
    # Get the absolute path
    basedir = os.path.abspath(os.path.dirname(__file__))
    instance_dir = os.path.join(basedir, 'instance')
    db_path = os.path.join(instance_dir, 'database.db')
    
    # Create instance directory if it doesn't exist
    os.makedirs(instance_dir, exist_ok=True)
    
    # Create empty database file
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        conn.close()
        print(f"Database file created at: {db_path}")
    
    # Create Flask app and tables
    app = create_app()
    
    with app.app_context():
        try:
            # Create all tables
            db.create_all()
            print("Tabelas criadas com sucesso!")
            
            # Check if categories already exist
            if Category.query.count() == 0:
                # Create default categories
                default_categories = [
                    {'name': 'Frutas e Vegetais', 'color': '#22C55E'},
                    {'name': 'Laticínios e Ovos', 'color': '#F97316'},
                    {'name': 'Carnes e Aves', 'color': '#EF4444'},
                    {'name': 'Padaria', 'color': '#EAB308'},
                    {'name': 'Produtos de Limpeza', 'color': '#3B82F6'},
                    {'name': 'Cuidados Pessoais', 'color': '#A855F7'},
                    {'name': 'Bebidas', 'color': '#06B6D4'},
                    {'name': 'Lanches', 'color': '#EC4899'},
                    {'name': 'Congelados', 'color': '#64748B'},
                    {'name': 'Itens Domésticos', 'color': '#6B7280'},
                ]
                
                for cat_data in default_categories:
                    category = Category(name=cat_data['name'], color=cat_data['color'])
                    db.session.add(category)
                
                db.session.commit()
                print("Default categories created!")
            
            print("Banco de dados inicializado com sucesso!")
            
        except Exception as e:
            print(f"Erro ao criar banco de dados: {e}")
            return False
    
    return True

if __name__ == '__main__':
    create_database()