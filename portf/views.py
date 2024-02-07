from django.shortcuts import render
from django.http import HttpResponse

def exchange(reqests):
    return render(reqests, 'index.html')