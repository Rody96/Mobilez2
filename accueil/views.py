from django.shortcuts import render, redirect
from accueil.models import Accueil


def accueil_index(request):
    # effectue une requete
    accueil = Accueil.objects.all()
    # send info to our template
    context = {
        'accueil': accueil
    }
    return render(request, 'accueil/index.html', context)


def accueil_detail(request, pk):
    accueil = Accueil.objects.get(pk=pk)
    context = {
        'accueil': accueil
    }
    return render(request, 'accueil/index_detail.html', context)


# Create your views here.

# def Accueil_view(request):
#     # page qu'on va chercher lors de la requête
#     return render(request, 'accueil/index.html')
