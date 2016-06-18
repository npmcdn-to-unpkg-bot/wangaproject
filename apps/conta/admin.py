from django.contrib import admin
from .models import Adresse, UserProfile
from django.contrib.auth.models import User
# Register your models here.

#admin.site.register(UserProfile)
admin.site.register(Adresse)
