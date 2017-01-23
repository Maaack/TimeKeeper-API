from django.conf.urls import url, include
from timelines import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'timelines', views.TimelineViewSet)
router.register(r'times', views.TimeViewSet)
router.register(r'time-links', views.TimeLinkViewSet)
router.register(r'time-keepers', views.TimeKeeperViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'actions', views.ActionViewSet)
router.register(r'activity', views.ActivityViewSet)
router.register(r'perspectives', views.PerspectiveViewSet)
router.register(r'elements', views.ElementViewSet)
router.register(r'actors', views.ActorViewSet)
router.register(r'sets', views.SetViewSet)
router.register(r'relative-positions', views.RelativePositionViewSet)
router.register(r'aliases', views.AliasViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]