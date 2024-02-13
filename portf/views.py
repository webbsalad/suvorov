from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.utils.translation import activate

# python manage.py collectstatic
# msgfmt -o django.mo django.po
# django-admin makemessages -l ru
def exchange(reqests):
    context = {
        'intest': 'intest'
    }
    return render(reqests, 'index.html', context)

def explanation(reqests):
    return render(reqests, 'explanation.html')

def prog(reqests):
    return render(reqests, 'prog.html')

def cw(reqests):
    return render(reqests, 'cw.html')

def set_language(request):
    if 'language' in request.GET:
        language = request.GET['language']
        activate(language)
    return redirect(request.META.get('HTTP_REFERER', '/'))