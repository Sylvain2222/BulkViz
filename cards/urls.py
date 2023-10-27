from django.contrib import admin
from django.urls import path
import cards.views as views



#index.html
urlpatterns = [
    path('bulk', views.card_view)
]

