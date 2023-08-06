from django.contrib.gis.geos import Point
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Place
from .serializers import PlaceSerializer


class PlaceListCreateView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def create(self, request, *args, **kwargs):
        latitude = request.data.get("latitude")
        longitude = request.data.get("longitude")
        serializer_data = {
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "coordinates": Point(float(longitude), float(latitude))
        }
        
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class PlaceDeleteView(generics.DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceSearchView(generics.ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        query = self.request.query_params.get("query", "")
        return Place.objects.annotate(
            search=SearchVector("name", "description")
        ).filter(search=query)


def home(request):
    return render(request, "index.html")
