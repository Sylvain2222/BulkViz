from django.urls import path, include
from cards import views
from rest_framework.routers import DefaultRouter

# import cards.views as views


# index.html
urlpatterns = [
    path('', views.index),
    path('bulk', views.bulk_view),
    path('cards', views.card_view),

]
