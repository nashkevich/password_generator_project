import random

import requests
from django.shortcuts import render
from django.http import HttpResponse

def home(request:requests.request):
    return render(request,'generator/home.html')

def password(request:requests.request):
    password = ''

    characters = 'qwertyuiopasdfghjklzxcvbnm'
    upper_characters = 'qwertyuiopasdfghjklzxcvbnm'.upper()
    spercial_charaters = '!@#$%^&*()_+=-[]{};:/?.,<>|'
    numbers = '1234567890'

    length = int(request.GET.get('length'))
    isUpper = request.GET.get('uppercase')
    isNumbers = request.GET.get('numbers')
    isSpecial = request.GET.get('special')

    if isUpper:
        characters += upper_characters
    if isSpecial:
        characters += spercial_charaters
    if isNumbers:
        characters += numbers

    for x in range(length):
        password += random.choice(characters)

    return render(request,'generator/password.html', {'password':password})