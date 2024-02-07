from django.shortcuts import render
from django.http import HttpResponse

def exchange(reqests):
    context = {
        'intest': 'intest'
    }
    return render(reqests, 'index.html', context)