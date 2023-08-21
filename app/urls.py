from django.urls import path

from . import views

urlpatterns = [
    path("properties/", views.PropertyListCreateView.as_view()),
    path("properties/<int:pk>/", views.PropertyRetrieveUpdateDestroyView.as_view()),
    path("bookings/", views.BookingListCreatView.as_view()),
    path("bookings/<int:pk>/", views.BookingRetrieveUpdateDestroyView.as_view()),
]
