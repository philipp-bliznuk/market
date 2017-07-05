from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from .serializers import ProductSerializer, VoteSerializer
from .models import Product, Vote


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class VoteViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
