from rest_framework import routers

from .viewsets import ProductViewSet, VoteViewSet


router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'votes', VoteViewSet)
