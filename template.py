# -*- coding: utf-8 -*-
import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Loop to get project name from user
while True:
    project_name = input("Enter your project name: ")
    if project_name.strip():  # Ensure project name is not empty or just spaces
        break

# Define the list of files to create
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"
]

# Create files and directories
for filepth in list_of_files:
    filepath = Path(filepth)
    filedir, filename = os.path.split(filepath)

    # Create directories if they don't exist
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)

    # Create empty file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        
    else:
        logging.info(f"File already exists: {filepath}")
