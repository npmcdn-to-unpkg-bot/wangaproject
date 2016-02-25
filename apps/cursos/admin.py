from django.contrib import admin

from django.contrib.auth.models import User
from .models import Curso, Membership, Turma, Modalidade
# Register your models here.

#admin.site.register(UserProfile)
#admin.site.register(Adresse)
admin.site.register(Curso)
admin.site.register(Modalidade)
admin.site.register(Turma)
admin.site.register(Membership)