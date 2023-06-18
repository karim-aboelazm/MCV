from django.contrib import admin
from .models import *

# getting all models from models.py file

our_models = [Car, Car_Diagnostic, Driver,MCVUser]

# adding our models to admin panal in database

for model in our_models:
    admin.site.register(model)
