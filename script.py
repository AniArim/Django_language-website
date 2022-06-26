#!/usr/bin/env python
#codding: utf-8

import os
import webbrowser

os.system('docker-compose build')
os.system('docker-compose create')
os.system('docker-compose start')
os.system('docker-compose exec web python manage.py migrate')
os.system('docker-compose exec web python manage.py loaddata db.json')

webbrowser.open('http://127.0.0.1:8000')



