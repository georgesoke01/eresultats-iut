from django.contrib import admin
from .models import Etudiant, Note, ConfigSite

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ["matricule", "nom", "prenoms", "sexe", "niveau_etude"]
    search_fields = ("matricule", "nom", "prenoms")
    list_filter = ["niveau_etude", "sexe"]
    ordering = ["nom"]

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("etudiant", "matiere", "note", "semestre")
    search_fields = ("etudiant__matricule", "matiere")
    list_filter = ["semestre"]
    ordering = ("etudiant", "semestre")
    
@admin.register(ConfigSite)
class ConfigSiteAdmin(admin.ModelAdmin):
    list_display = ('reclamations_actives',)
