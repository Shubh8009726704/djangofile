from django.contrib import admin
from .models import *

@admin.register(register)

class registerAdmin(admin.ModelAdmin):
    list_display=('id','name','age','phone','email')
    

# Register your models here.
