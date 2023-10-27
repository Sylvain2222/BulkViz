from django.shortcuts import render, redirect
from django.http import JsonResponse
import cards.models
from cards.test_run import *
import json

# Create your views here.

def card_view(request):
    cquad4 = cards.models.Element
    cquad4.name = d["CQUAD4"][0]['name']
    cquad4.id = d["CQUAD4"][0]['id']
    cquad4.property = d["CQUAD4"][0]['property']

    json_str = json.dumps(cquad4.name + ":" + cquad4.id + "," + cquad4.property, indent=2)
    # return JsonResponse(cquad4.toDict())
    return JsonResponse(json_str, safe=False)


def bulk_view(request):
    bulk_json = d
    return JsonResponse(bulk_json)


def cquad4_view(request):
    first_cquad4 = d["CQUAD4"][0]
    return JsonResponse(first_cquad4)
