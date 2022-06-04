# HIT4002022

HIT 400 2021-2022 (Takudzwa J Chigwida H180073W)

# Project installation

pip install django
pip install recordlinkage

# Create virtual environment called 400venv

python -m venv 400venv

# For Linux/Mac (Running Program)

source 400venv/bin/activate

# For Windows (Running Program)

400venv\scripts\activate

pip install -r requirements.txt

pip install recordlinkage

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

# For Admin Login

Run the following in terminal:

python manage.py createsuperuser
