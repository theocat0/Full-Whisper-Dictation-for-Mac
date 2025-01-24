#!/bin/bash

# Exit on error
set -e

echo "🚀 Building Whisper Dictation for Mac..."

# Ensure we're in a virtual environment
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build dist

# Build the application
echo "🔨 Building application..."
python setup.py py2app

echo "✨ Build complete! Application is in the dist/ directory."
echo "To install, drag 'Whisper Dictation.app' from the dist/ folder to your Applications folder." 