#!/usr/bin/env python3
"""
WSGI entry point for production deployment
"""

import os
from app import create_app

# Determine configuration based on environment
if os.environ.get('FLASK_ENV') == 'production' or os.environ.get('DATABASE_URL'):
    from production_config import ProductionConfig
    config_class = ProductionConfig
else:
    from config import Config
    config_class = Config

# Create the Flask application with appropriate config
app = create_app(config_class)

if __name__ == "__main__":
    # This is for local testing only
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)