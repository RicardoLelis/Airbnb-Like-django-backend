# from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Amenity, AmenityType, Booking, Photo, Property, PropertyType, Review, Room, RoomBooking, User
from .permissions import IsOwnerOrReadOnly, IsAuthenticatedOrReadOnlyForCreate
from .serializers import (
    AmenitySerializer,
    AmenityTypeSerializer,
    BookingSerializer,
    PhotoSerializer,
    PropertySerializer,
    PropertyTypeSerializer,
    ReviewSerializer,
    RoomBookingSerializer,
    RoomSerializer,
    UserSerializer,
)


class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticatedOrReadOnlyForCreate]

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)


class PropertyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class BookingListCreatView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Booking.objects.filter(guest=self.request.user)

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)


class BookingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Booking.objects.filter(guest=self.request.user)
