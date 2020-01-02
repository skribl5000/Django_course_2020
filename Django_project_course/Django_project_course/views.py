from django.shortcuts import render

def home_view(request):
    context = {
        'name': 'Ruslan Talypov',
    }
    return render(request, 'home.html', context)