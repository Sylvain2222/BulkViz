from django.urls import path
from cards import views

# import cards.views as views


# index.html
urlpatterns = [
    path('bulk', views.card_view)
]
