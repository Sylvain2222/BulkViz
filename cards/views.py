from django.shortcuts import render, redirect
#from flask import Flask, request


# Create your views here.
def index(request):
    return render(request, 'cards/index.html',context={})
