from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('devis/', views.devis, name='devis'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('mentions-legales/', views.mentions_legales, name='mentions_legales'),
    path('qui-sommes-nous/', views.a_propos, name='a_propos'),
]
