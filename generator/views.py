import random
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'visibil':"hidden"})

def password(request):
    
    characteres = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        characteres.extend(list('ABCDEFGHIJKLQMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characteres.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characteres.extend(list('0123456789'))
        
    length = int(request.GET.get('length', 12))
    showing = "text"
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characteres)

    return render(request, 'generator/home.html', {'password':thepassword, 'visibility': showing})
