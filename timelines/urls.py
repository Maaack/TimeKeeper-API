from django.conf.urls import url, include
from timelines import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'timelines', views.TimelineViewSet)
router.register(r'time-keepers', views.TimeKeeperViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]