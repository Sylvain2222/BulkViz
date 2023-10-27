from django.shortcuts import render, redirect
#from flask import Flask, request
from cards import models

# Create your views here.
# def index(request):
#     return render(request, 'cards/index.html',context={})


def card_view(request):
    # card = {
    #     'name': 'CQUAD4',
    #     'id': 99,
    #     'count': 789,
    # }
    card = models.Card()
    card.name = "CQUAD4"
    card.id = 12
    card.count = 987

    return JsonResponse(card.toDict())