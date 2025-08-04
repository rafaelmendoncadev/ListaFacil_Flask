import os
import logging
from config import Config

class ProductionConfig(Config):
    """Production configuration with enhanced error handling"""
    
    # Ensure we're in production mode
    DEBUG = False
    TESTING = False
    
    # Enhanced logging
    LOG_LEVEL = logging.INFO
    
    # Database configuration with better error handling
    @staticmethod
    def init_app(app):
        Config.init_app(app)
        
        # Configure logging for production
        if not app.debug and not app.testing:
            # Set up logging
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
            )
            
            app.logger.setLevel(logging.INFO)
            app.logger.info('ListaFácil startup')
        
        # Database initialization with retry logic
        from app import db
        from flask_migrate import upgrade
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # Ensure database tables exist
                upgrade()
                app.logger.info('Database migrations completed successfully')
                
                # Create default categories if needed
                with app.app_context():
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
                        app.logger.info(f'Created {len(default_categories)} default categories')
                
                break  # Success, exit retry loop
                
            except Exception as e:
                app.logger.error(f'Database initialization attempt {attempt + 1} failed: {str(e)}')
                if attempt == max_retries - 1:
                    app.logger.error('All database initialization attempts failed')
                    # Don't raise exception, let app start anyway
                else:
                    import time
                    time.sleep(2)  # Wait before retry