# Fast Api Project

## Fast Api Project Installation and Usage Instructions

This document provides step-by-step instructions for installing the Django project, creating a virtual environment, installing dependencies, and running the project.

## Requirements

The following programs must be installed on your computer:

- **pip (Python package manager)**
- **Virtualenv (or other virtual environment manager)**
- **Go to** (to clone the project)

## Setting Up the Project

### 1. Download the Project with Git

First of all, clone the project to your computer using Git:

```bash
git clone https://github.com/MetinQardasov11/FastAPI-Lessons.git
```
<br>

### 2. Create a Virtual Environment

#### MacOS / Linux:

```bash
python3 -m venv env
source env/bin/activate
```

#### Windows:

```bash
py -m venv env
.\env\Scripts\activate
```
<br>

### 3. Installing the Necessary Packages

```bash
pip install -r requirements.txt
```
<br>

### 4. Running the Project

#### MacOS / Linux / Windows:

```bash
uvicorn file_name:app_name --reload
```