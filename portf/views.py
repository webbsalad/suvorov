from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

# python manage.py collectstatic
def exchange(reqests):
    context = {
        'intest': 'intest'
    }
    return render(reqests, 'index.html', context)

def explanation(reqests):
    return render(reqests, 'explanation.html')

def prog(reqests):
    return render(reqests, 'prog.html')

def kp(reqests):
    return render(reqests, 'kp.html')