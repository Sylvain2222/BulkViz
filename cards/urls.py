from django.urls import path
from cards import views

# import cards.views as views


# index.html
urlpatterns = [
    path('bulk', views.bulk_view),
    path('card', views.card_view),
    path('cquad4', views.cquad4_view)
]
