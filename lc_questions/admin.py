from django.contrib import admin

# Register your models here.
# questions/admin.py

from django.contrib import admin
from .models import Question

admin.site.register(Question)
