from django.shortcuts import render, redirect
#from flask import Flask, request
from cards import models
from django.http import JsonResponse

# Create your views here.

def card_view(request):

    card = models.Card()
    card.name = "CQUAD4"
    card.id = 12
    card.count = 987

    return JsonResponse(card.toDict())