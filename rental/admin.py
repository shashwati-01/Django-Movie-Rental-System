from django.contrib import admin
from .models import Customer, Movie, Invoice

admin.site.register(Customer)
admin.site.register(Movie)
admin.site.register(Invoice)
