#!/usr/bin/env bash

# Installa le dipendenze
pip install -r requirements.txt

# Raccoglie i file statici
python manage.py collectstatic --noinput

# Applica le migrazioni
python manage.py migrate
