from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of all travel listings.",
        responses={200: ListingSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of all bookings.",
        responses={200: BookingSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)