#!/bin/bash

echo "PyTris Linux/MacOS Build Script Version 1.0.0, Made by grqphical"

if [ ! -d "./venv" ]; then
    echo "Creating virtual env..."
    python3 -m venv venv > /dev/null
fi

echo "Installing Dependencies..."
source ./venv/bin/activate > /dev/null
pip install pygame-ce pyinstaller Pillow > /dev/null

echo "Building PyTris"
pyinstaller PyTris.spec

echo ""
echo "PyTris has been built in dist/. Make sure to include all the asset folders when distributing"