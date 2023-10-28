from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from cards.test_run import *
import json


# from cards.serializers import CardSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import viewsets
# from rest_framework import serializers


# Create your views here.
def index(request):
    return render(request, 'cards/index.html', context={"data": dict_bulk})


def bulk_view(request):
    # bulk_json = dict_bulk
    # return JsonResponse(bulk_json)
    return HttpResponse(json.dumps(dict_bulk, cls=ComplexEncoder), content_type="application/json")


def card_view(request):
    return HttpResponse(json.dumps(first_cards, cls=ComplexEncoder), content_type="application/json")


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Element, Property, Material)):
            return obj.__dict__
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
