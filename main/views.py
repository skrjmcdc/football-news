from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2406357684',
        'name': 'Muhammad Ibaadi Ilmi',
        'class': 'PBP A',
    }

    return render(request, "main.html", context)
