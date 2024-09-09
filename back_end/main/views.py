from . import models
from rest_framework import generics
from . import serializers
# Create your views here.

class VendorList(generics.ListAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer