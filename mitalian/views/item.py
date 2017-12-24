from django.shortcuts import render


def item(request, pk):
    return render(request, 'home.html')
