from django.urls import path
from django.conf.urls import include
from timekeeper import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'timelines', views.TimelineViewSet)
router.register(r'time-keepers', views.TimeKeeperViewSet)
router.register(r'axe', views.AxisViewSet)
router.register(r'positions', views.PositionViewSet)
router.register(r'notes', views.NoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
]