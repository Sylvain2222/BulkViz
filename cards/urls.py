from django.urls import path, include
from cards import views
from rest_framework.routers import DefaultRouter

# import cards.views as views


# index.html
urlpatterns = [
    path('', views.index),
    path('bulk', views.bulk_view),
    path('card', views.card_view),
    path('cquad4', views.cquad4_view),

]
