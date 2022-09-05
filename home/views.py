from django.shortcuts import render
from django.utils.translation import activate


def index(request):
    activate('fa') # i18n activate
    return render(request, 'index.html', {})
