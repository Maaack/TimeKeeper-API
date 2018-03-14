from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'timelines', views.TimelineViewSet)
router.register(r'time-keepers', views.TimeKeeperViewSet)
router.register(r'axe', views.AxisViewSet)
router.register(r'positions', views.PositionViewSet)
router.register(r'notes', views.NoteViewSet)

urlpatterns = router.urls