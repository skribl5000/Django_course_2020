from django.shortcuts import render

def home_view(request):
    context = {
        'name': 'Ruslan Talypov',
        'range': range(10),
        
    }
    return render(request, 'home.html', context)