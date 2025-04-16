from django.urls import path
from .views import recherche_resultats, export_pdf, deposer_reclamation, confirmation_reclamation

urlpatterns = [
    path("resultats/<slug:slug>/", recherche_resultats, name='recherche_resultats'),
    path('export_pdf/<str:matricule>/', export_pdf, name='export_pdf'),
    path("reclamation/<str:matricule>/", deposer_reclamation, name="deposer_reclamation"),
    path("confirmation-reclamation/", confirmation_reclamation, name="confirmation_reclamation"),

]
