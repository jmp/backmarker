from rest_framework.routers import DefaultRouter

from .api.viewsets.circuit_viewset import CircuitViewSet
from .api.viewsets.constructor_result_viewset import ConstructorResultViewSet
from .api.viewsets.constructor_standing_viewset import ConstructorStandingViewSet
from .api.viewsets.constructor_viewset import ConstructorViewSet
from .api.viewsets.driver_standing_viewset import DriverStandingViewSet
from .api.viewsets.driver_viewset import DriverViewSet
from .api.viewsets.lap_time_viewset import LapTimeViewSet
from .api.viewsets.pit_stop_viewset import PitStopViewSet
from .api.viewsets.qualifying_viewset import QualifyingViewSet
from .api.viewsets.race_viewset import RaceViewSet
from .api.viewsets.result_viewset import ResultViewSet
from .api.viewsets.season_viewset import SeasonViewSet
from .api.viewsets.status_viewset import StatusViewSet

router = DefaultRouter()

router.register(r"circuits", CircuitViewSet)
router.register(r"constructors", ConstructorViewSet)
router.register(r"constructor_results", ConstructorResultViewSet)
router.register(r"constructor_standings", ConstructorStandingViewSet)
router.register(r"drivers", DriverViewSet)
router.register(r"driver_standings", DriverStandingViewSet)
router.register(r"lap_times", LapTimeViewSet)
router.register(r"qualifyings", QualifyingViewSet)
router.register(r"pit_stops", PitStopViewSet)
router.register(r"races", RaceViewSet)
router.register(r"results", ResultViewSet)
router.register(r"seasons", SeasonViewSet)
router.register(r"statuses", StatusViewSet)

urlpatterns = router.urls
