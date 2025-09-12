from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'title' : 'ATLAS',
        'npm' : '2406407373',
        'name': 'Andrew Wanarahardja',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)