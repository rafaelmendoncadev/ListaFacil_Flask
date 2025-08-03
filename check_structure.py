#!/usr/bin/env python3
"""
Simple script to check if the project structure is correct
and all required files are present.
"""

import os
import sys

def check_file_exists(filepath, description):
    """Check if a file exists and print status."""
    if os.path.exists(filepath):
        print(f"✓ {description}: {filepath}")
        return True
    else:
        print(f"✗ {description}: {filepath} - MISSING")
        return False

def check_directory_exists(dirpath, description):
    """Check if a directory exists and print status."""
    if os.path.exists(dirpath) and os.path.isdir(dirpath):
        print(f"✓ {description}: {dirpath}")
        return True
    else:
        print(f"✗ {description}: {dirpath} - MISSING")
        return False

def main():
    """Main function to check project structure."""
    print("ListaFácil - Project Structure Check")
    print("=" * 40)
    
    all_good = True
    
    # Check main files
    files_to_check = [
        ("app.py", "Main application file"),
        ("config.py", "Configuration file"),
        ("requirements.txt", "Dependencies file"),
        ("init_db.py", "Database initialization script"),
        ("README.md", "Documentation"),
        (".env", "Environment variables"),
    ]
    
    for filename, description in files_to_check:
        if not check_file_exists(filename, description):
            all_good = False
    
    # Check directories
    directories_to_check = [
        ("app", "Main application directory"),
        ("app/auth", "Authentication blueprint"),
        ("app/main", "Main blueprint"),
        ("app/templates", "Templates directory"),
        ("app/templates/auth", "Auth templates"),
        ("app/static", "Static files directory"),
        ("app/static/js", "JavaScript files"),
        ("app/static/css", "CSS files"),
        ("instance", "Instance directory for database"),
    ]
    
    for dirname, description in directories_to_check:
        if not check_directory_exists(dirname, description):
            all_good = False
    
    # Check app files
    app_files = [
        ("app/__init__.py", "App factory"),
        ("app/models.py", "Database models"),
        ("app/forms.py", "WTForms forms"),
        ("app/auth/__init__.py", "Auth blueprint init"),
        ("app/auth/routes.py", "Auth routes"),
        ("app/auth/forms.py", "Auth forms"),
        ("app/main/__init__.py", "Main blueprint init"),
        ("app/main/routes.py", "Main routes"),
    ]
    
    for filename, description in app_files:
        if not check_file_exists(filename, description):
            all_good = False
    
    # Check templates
    templates = [
        ("app/templates/base.html", "Base template"),
        ("app/templates/index.html", "Home page"),
        ("app/templates/dashboard.html", "Dashboard"),
        ("app/templates/create_list.html", "Create list form"),
        ("app/templates/list_detail.html", "List detail page"),
        ("app/templates/categories.html", "Categories page"),
        ("app/templates/purchase_history.html", "Purchase history"),
        ("app/templates/auth/login.html", "Login page"),
        ("app/templates/auth/register.html", "Registration page"),
    ]
    
    for filename, description in templates:
        if not check_file_exists(filename, description):
            all_good = False
    
    # Check static files
    static_files = [
        ("app/static/js/main.js", "Main JavaScript file"),
    ]
    
    for filename, description in static_files:
        if not check_file_exists(filename, description):
            all_good = False
    
    print("\n" + "=" * 40)
    if all_good:
        print("✓ All files and directories are present!")
        print("\nNext steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Initialize database: python init_db.py")
        print("3. Run application: python app.py")
        print("4. Open http://localhost:5000 in your browser")
    else:
        print("✗ Some files or directories are missing!")
        print("Please check the missing items above.")
    
    return 0 if all_good else 1

if __name__ == "__main__":
    sys.exit(main())