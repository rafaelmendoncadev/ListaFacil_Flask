# Installation Guide

## Prerequisites

Make sure you have Python 3.8+ installed on your system.

## Step-by-Step Installation

### 1. Install pip (if not available)

If pip is not installed, download and install it:

```bash
# Download get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Install pip
python get-pip.py
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize Database

```bash
python init_db.py
```

### 5. Run the Application

```bash
python app.py
```

### 6. Access the Application

Open your web browser and go to: `http://localhost:5000`

## Troubleshooting

### If pip is not available:
1. Reinstall Python with pip included
2. Or manually install pip using get-pip.py

### If virtual environment fails:
```bash
# Alternative virtual environment creation
python -m venv --system-site-packages venv
```

### If database initialization fails:
1. Make sure the instance directory exists
2. Check file permissions
3. Try running as administrator (Windows) or with sudo (Linux/macOS)

### Common Issues:

1. **Port already in use**: Change the port in app.py or kill the process using the port
2. **Permission errors**: Run with appropriate permissions
3. **Module not found**: Make sure all dependencies are installed in the correct environment

## Production Deployment

For production deployment, consider:

1. Using a production WSGI server (Gunicorn, uWSGI)
2. Setting up a reverse proxy (Nginx, Apache)
3. Using environment variables for configuration
4. Setting up SSL/HTTPS
5. Using a production database (PostgreSQL, MySQL)
6. Implementing logging and monitoring