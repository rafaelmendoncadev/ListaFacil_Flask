from app import create_app, db
from app.models import User, List, Item, Category, PurchaseHistory

def init_database():
    """Initialize the database with default categories."""
    app = create_app()
    
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if categories already exist
        if Category.query.count() == 0:
            # Create default categories
            default_categories = [
                {'name': 'Fruits & Vegetables', 'color': '#22C55E'},
                {'name': 'Dairy & Eggs', 'color': '#F97316'},
                {'name': 'Meat & Poultry', 'color': '#EF4444'},
                {'name': 'Bakery', 'color': '#EAB308'},
                {'name': 'Cleaning Supplies', 'color': '#3B82F6'},
                {'name': 'Personal Care', 'color': '#A855F7'},
                {'name': 'Beverages', 'color': '#06B6D4'},
                {'name': 'Snacks', 'color': '#EC4899'},
                {'name': 'Frozen Foods', 'color': '#64748B'},
                {'name': 'Household Items', 'color': '#6B7280'},
            ]
            
            for cat_data in default_categories:
                category = Category(name=cat_data['name'], color=cat_data['color'])
                db.session.add(category)
            
            db.session.commit()
            print("Default categories created!")
        
        print("Banco de dados inicializado com sucesso!")

if __name__ == '__main__':
    init_database()