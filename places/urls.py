from django.urls import path
from .views import PlaceListCreateView, PlaceDeleteView, PlaceSearchView, home

urlpatterns = [
    path("", home),
    path("api/places/", PlaceListCreateView.as_view(), name="place-list"),
    path("api/places/<int:pk>/", PlaceDeleteView.as_view(), name="place-delete"),
    path("api/places/search/", PlaceSearchView.as_view(), name="place-search"),
]
