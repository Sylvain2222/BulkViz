from django.urls import path,include
from cards import views
from rest_framework.schemas import get_schema_view
# from rest_framework.routers import DefaultRouter
# import cards.views as views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# index.html
urlpatterns = [
    # path('', views.index),
    path('bulk', views.bulk_view),
    path('cards', views.top_cards_view),
    # path('openapi', get_schema_view(
    #     title="Your Project",
    #     description="API for all things …",
    #     version="1.0.0"
    # ), name='openapi-schema'),
    path("bulk/schema/", SpectacularAPIView.as_view(),name="schema"),
    path("bulk/schema/docs/",SpectacularSwaggerView.as_view(url_name="schema")),
]
