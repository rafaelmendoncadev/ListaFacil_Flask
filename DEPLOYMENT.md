# Deployment Guide for ListaFácil

## Railway Deployment (Recommended)

### Prerequisites
- GitHub account
- Railway account (https://railway.app)
- Git installed locally

### Deploy to Railway

1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "Prepare for Railway deployment"
   git push origin main
   ```

2. **Connect to Railway**:
   - Go to https://railway.app
   - Sign in with GitHub
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your ListaFácil repository

3. **Configure Environment Variables**:
   In Railway dashboard, go to your project > Variables and add:
   ```
   SECRET_KEY=your-super-secret-key-here
   FLASK_ENV=production
   FLASK_DEBUG=False
   ```

4. **Database Setup**:
   - Railway will automatically provision a PostgreSQL database
   - The DATABASE_URL will be automatically set

5. **Deploy**:
   - Railway will automatically build and deploy your app
   - Your app will be available at the provided Railway URL

### Railway Configuration Files

The following files are configured for Railway deployment:
- `Procfile`: Defines how to start the application
- `railway.json`: Railway-specific configuration
- `runtime.txt`: Specifies Python version
- `requirements.txt`: Includes production dependencies (gunicorn, psycopg2-binary)

## Quick Start (Development)

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Local Development Setup

1. **Navigate to project directory**:
   ```bash
   cd ListaFacil
   ```

2. **Create virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # Activate on Windows:
   venv\Scripts\activate
   
   # Activate on macOS/Linux:
   source venv/bin/activate
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

6. **Access the application**:
   Open your web browser and go to: http://localhost:5000

## Production Deployment

### Option 1: Simple Production Setup

1. **Install production dependencies**:
   ```bash
   pip install gunicorn
   ```

2. **Set environment variables**:
   ```bash
   export SECRET_KEY="your-very-secure-secret-key-here"
   export DATABASE_URL="sqlite:///instance/database.db"
   export FLASK_ENV="production"
   ```

3. **Run with Gunicorn**:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

### Option 2: Docker Deployment

Create a `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python init_db.py

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:
```bash
docker build -t listafacil .
docker run -p 5000:5000 listafacil
```

### Option 3: Cloud Platform Deployment

#### Heroku
1. Create `Procfile`:
   ```
   web: gunicorn app:app
   ```

2. Create `runtime.txt`:
   ```
   python-3.11.8
   ```

3. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

#### Railway/Render
1. Connect your GitHub repository
2. Set environment variables in the platform dashboard
3. Deploy automatically

## Environment Variables

For production, set these environment variables:

```bash
SECRET_KEY=your-super-secret-key-change-this-in-production
DATABASE_URL=sqlite:///instance/database.db
FLASK_ENV=production
```

## Database Options

### SQLite (Default - Good for small to medium usage)
```python
DATABASE_URL=sqlite:///instance/database.db
```

### PostgreSQL (Recommended for production)
```python
DATABASE_URL=postgresql://username:password@localhost/listafacil
```

### MySQL
```python
DATABASE_URL=mysql://username:password@localhost/listafacil
```

## Security Considerations

1. **Change the secret key** in production
2. **Use HTTPS** in production
3. **Set up proper database backups**
4. **Use environment variables** for sensitive data
5. **Enable CSRF protection** (already implemented)
6. **Set up monitoring and logging**

## Performance Optimization

1. **Use a production database** (PostgreSQL recommended)
2. **Set up Redis** for session storage (optional)
3. **Enable gzip compression**
4. **Use a CDN** for static files
5. **Set up database connection pooling**

## Monitoring and Maintenance

1. **Set up logging**:
   ```python
   import logging
   logging.basicConfig(level=logging.INFO)
   ```

2. **Monitor disk space** (especially for SQLite)
3. **Set up automated backups**
4. **Monitor application performance**
5. **Keep dependencies updated**

## Troubleshooting

### Common Issues

1. **Database file permissions**:
   ```bash
   chmod 664 instance/database.db
   chown www-data:www-data instance/database.db
   ```

2. **Port already in use**:
   ```bash
   lsof -ti:5000 | xargs kill -9
   ```

3. **Module not found errors**:
   - Ensure virtual environment is activated
   - Reinstall dependencies: `pip install -r requirements.txt`

4. **Database initialization fails**:
   - Check file permissions
   - Ensure instance directory exists
   - Try running as administrator/sudo

### Support

For issues and questions:
1. Check the logs first
2. Verify all dependencies are installed
3. Check file permissions
4. Ensure all environment variables are set

## Backup Strategy

### SQLite Backup
```bash
# Simple file backup
cp instance/database.db instance/database_backup.db

# SQL dump
sqlite3 instance/database.db .dump > backup.sql
```

### PostgreSQL Backup
```bash
pg_dump listafacil > backup.sql
```

## Update Procedure

1. **Backup database**
2. **Pull latest code**
3. **Update dependencies**: `pip install -r requirements.txt`
4. **Run database migrations** (if any)
5. **Restart application**
6. **Test functionality**

---

**ListaFácil** is now ready for deployment! 🚀