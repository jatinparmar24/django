from rest_framework import routers
from .views import MovieViewSet

router = routers.SimpleRouter()
router.register(r'movie', MovieViewSet, basename='movie')

urlpatterns = router.urls
