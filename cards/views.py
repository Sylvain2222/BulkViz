from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import cards.models
from cards.test_run import *
import json
from cards.serializers import CardSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import serializers


# Create your views here.
def index(request):
    return render(request, 'cards/index.html', context={"data":d})


# def card_view(request):
#     cquad4 = cards.models.Element
#     cquad4.name = d["CQUAD4"][0]['name']
#     cquad4.id = d["CQUAD4"][0]['id']
#     cquad4.property = d["CQUAD4"][0]['property']
#     cquad4.grids = d["CQUAD4"][0]['grids']
#     cquad4.orientation = d["CQUAD4"][0]['orientation']
#
#     json_str = json.dumps(
#         cquad4.name + ":" + cquad4.id + "," + cquad4.property + "," + cquad4.grids + "," + cquad4.orientation, indent=2)
#     # return JsonResponse(cquad4.toDict())
#     return JsonResponse(json_str, safe=False)


def bulk_view(request):
    bulk_json = d
    return JsonResponse(bulk_json)


def cquad4_view(request):
    return HttpResponse(json.dumps(first_cards,cls=ComplexEncoder), content_type="application/json")


def card_view(request):
    # cquad4 = cards.models.Element(d["CQUAD4"][0]['name'], d["CQUAD4"][0]['id'], d["CQUAD4"][0]['property'],
    #                               d["CQUAD4"][0]['grids'], d["CQUAD4"][0]['orientation'])

    # return JsonResponse(cquad4.toDict())
    return HttpResponse(json.dumps(d,cls=ComplexEncoder), content_type="application/json")

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Element,Property,Material)):
            return obj.__dict__
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

