from django.shortcuts import render
from django.http import HttpResponse

def joy(request):
    return HttpResponse(""" Habibi com to Dubain <br>
    <a href='/car/'>Mashina</a> <br>
    <a href='/ish/'>Kasbi</a> <br>
    <a href='/soqqa/'>Maoshi</a>
    """)

def car(request):
    return HttpResponse(""" BMW m8 Competition  <br>
    <a href='/'>Amerika</a> <br>
    <a href='/ish/'>Kasbi</a><br>
    <a href='/soqqa/'>Maoshi</a>
    """)

def ish(request):
    return HttpResponse(""" Full-stack developer <br>
    <a href='/'>Amerika</a> <br>
    <a href='/car/'>Mashina</a> <br>
    <a href='/soqqa/'>Maoshi</a>
    """)

def soqqa(request):
    return HttpResponse(""" My monthly salary 300 000 $ <br>
    <a href='/'>Amerika</a> <br>
    <a href='/car/'>Mashina</a> <br>
    <a href='/ish/'>Kasbi</a>
    """)