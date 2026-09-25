from django.contrib import admin
from .models import Devis, Realisation

@admin.register(Devis)
class DevisAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'prestation', 'budget', 'date_envoi')
    list_filter = ('prestation', 'date_envoi')
    search_fields = ('nom', 'email', 'description')

@admin.register(Realisation)
class RealisationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'date_creation', 'publie')
    list_filter = ('categorie', 'publie', 'date_creation')
    search_fields = ('titre', 'description')
    prepopulated_fields = {'slug': ('titre',)}