from django.contrib import admin
from .models import ExamConcours

@admin.register(ExamConcours)
class ExamConcoursAdmin(admin.ModelAdmin):
    list_display = ('numero_ordre', 'titre', 'description', 'statut')
    #prepopulated_fields = {'slug': ('titre',)}