from django.urls import path
from .views import index, all_result

urlpatterns = [
    path("", index, name="index"),
    path("voir_tout", all_result, name="voir_tout"),
    #path("resultats/<slug:slug>/", resultat_examen, name="resultat_examen")
]