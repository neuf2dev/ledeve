from django.db import models

class Devis(models.Model):
    SERVICES = [
        ('WEB', 'Application Web'),
        ('MOBILE', 'Application Mobile'),
        ('VITRINE', 'Site Vitrine'),
        ('CONSEIL', 'Audit & Consulting'),
    ]

    nom = models.CharField(max_length=100)
    email = models.EmailField()
    prestation = models.CharField(max_length=50, choices=SERVICES)
    description = models.TextField()
    budget = models.CharField(max_length=50)
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Devis de {self.nom} - {self.prestation}"


class Realisation(models.Model):
    titre = models.CharField(max_length=200, verbose_name="Titre du projet")
    slug = models.SlugField(unique=True, blank=True)
    categorie = models.CharField(max_length=100, verbose_name="Catégorie (ex: E-commerce, Vitrine, Automatisation)")
    description = models.TextField(verbose_name="Description du projet")
    image = models.ImageField(upload_to='realisations/', verbose_name="Visuel du projet")
    url_site = models.URLField(blank=True, null=True, verbose_name="Lien vers le projet")
    date_creation = models.DateField(auto_now_add=True, verbose_name="Date de réalisation")
    publie = models.BooleanField(default=True, verbose_name="Publié sur le site")

    def __str__(self):
        return self.titre