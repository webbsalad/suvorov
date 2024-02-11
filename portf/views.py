from django.shortcuts import render
from django.http import HttpResponse

# python manage.py collectstatic
def exchange(reqests):
    context = {
        'intest': 'intest'
    }
    return render(reqests, 'index.html', context)

def explanation(reqests):
    return render(reqests, 'explanation.html')

def prog(reqests):
    return render(reqests, 'stack.html')