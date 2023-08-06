from django.test import TestCase
from django.urls import reverse
from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.test import APIClient
from .models import Place


class PlaceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        coordinates = Point(float("18.5204378"), float("73.8567437"))
        self.place_data = {
            "name": "Test",
            "description": "A test place",
            "coordinates": coordinates

        }
        self.create_place = {
            "name": "Pune",
            "description": "A test place",
            "latitude": "18.5204303",
            "longitude": "73.8567437"
        }
        self.place = Place.objects.create(**self.place_data)

    def test_get_all_places(self):
        response = self.client.get(reverse("place-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.place.name)

    def test_create_place(self):
        response = self.client.post(reverse("place-list"), self.create_place)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Place.objects.count(), 2)

    def test_search_places(self):
        search_query = "Test"
        response = self.client.get(reverse("place-search"), {"query": search_query})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.place.name)

    def test_delete_place(self):
        response = self.client.delete(reverse("place-delete", args=[self.place.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Place.objects.count(), 0)
