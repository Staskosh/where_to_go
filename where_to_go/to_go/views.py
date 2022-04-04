from django.shortcuts import render


def show_who_is_online(request):
    return render(request, 'index.html')

# Create your views here.
