from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from cards.run_app import *
import json


# from cards.serializers import CardSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import viewsets
# from rest_framework import serializers


# View of index page
def index(request):
    return render(request, 'cards/index.html', context={"bulk": dict_bulk})


# view of all cards
def bulk_view(request):
    # json.dumps() convert objects into a json string
    return HttpResponse(json.dumps(dict_bulk, cls=ComplexEncoder), content_type="application/json")


# View of the first card of each type of card
def top_cards_view(request):
    # json.dumps() convert dict into a json string
    return HttpResponse(json.dumps(first_cards, cls=ComplexEncoder), content_type="application/json")


# Encoder to convert object to JSON
# from https://docs.python.org/fr/3/library/json.html
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Element, Property, Material)):
            return obj.__dict__
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
