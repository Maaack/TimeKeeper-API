from django.conf.urls import url, include
from timekeeper_base import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'timelines', views.TimelineViewSet)
router.register(r'times', views.TimeViewSet)
router.register(r'time-links', views.TimeLinkViewSet)
router.register(r'time-keepers', views.TimeKeeperViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]