#!/bin/bash
# Railway deployment script
# This script handles the Python command compatibility

echo "Starting Railway deployment initialization..."

# Try python3 first, then python
if command -v python3 &> /dev/null; then
    echo "Using python3..."
    python3 railway_init.py
elif command -v python &> /dev/null; then
    echo "Using python..."
    python railway_init.py
else
    echo "ERROR: Neither python3 nor python found!"
    exit 1
fi

echo "Railway initialization completed!"