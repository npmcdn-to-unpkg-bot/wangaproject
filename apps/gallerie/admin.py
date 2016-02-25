from django.contrib import admin
from .models import Album,Photo
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["titulo","descricao","publicar","autor"]


class PhotoAdmin(admin.ModelAdmin):
    # search_fields = ["title"]
    list_display = ["nome","isCover","album","created"]
    list_filter = ["album"]

admin.site.register(Album,AlbumAdmin)
admin.site.register(Photo,PhotoAdmin)