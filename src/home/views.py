from django.shortcuts import render

def index(request):
    """Pagina Inicial"""

    return render(request, 'home.html')
