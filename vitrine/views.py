from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Devis, Realisation
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    # On récupère les réalisations publiées pour les afficher dynamiquement
    realisations = Realisation.objects.filter(publie=True).order_by('-date_creation')
    return render(request, 'vitrine/index.html', {'realisations': realisations})

def devis(request):
    if request.method == 'POST':
        nom = request.POST.get('nom', '').strip()
        email = request.POST.get('email', '').strip()
        prestation = request.POST.get('prestation', '').strip()
        description = request.POST.get('description', '').strip()
        budget = request.POST.get('budget', '').strip()

        if nom and email and prestation:
            # Enregistrement dans la base de données
            Devis.objects.create(
                nom=nom,
                email=email,
                prestation=prestation,
                description=description,
                budget=budget
            )

            # Envoi de l'e-mail via Brevo SMTP
            sujet = f"Nouvelle demande de devis de {nom} ({prestation})"
            message = f"Nom : {nom}\nEmail : {email}\nPrestation : {prestation}\nBudget : {budget}\n\nDescription :\n{description}"
            
            try:
                send_mail(
                    subject=sujet,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Erreur d'envoi d'e-mail : {e}")

            messages.success(request, f"Merci {nom}, votre demande de devis a bien été transmise !")
            return redirect('devis')
        else:
            messages.error(request, "Veuillez remplir les champs obligatoires.")

    return render(request, 'vitrine/devis.html')

def portfolio(request):
    # On récupère les réalisations publiées pour les afficher dynamiquement
    realisations = Realisation.objects.filter(publie=True).order_by('-date_creation')
    return render(request, 'vitrine/portfolio.html', {'realisations': realisations})

def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom', '').strip()
        messages.success(request, f"Merci {nom}, votre message a bien été envoyé !")
        return redirect('contact')
    return render(request, 'vitrine/contact.html')

def mentions_legales(request):
    return render(request, 'vitrine/mentions_legales.html')

def a_propos(request):
    return render(request, 'vitrine/a_propos.html')