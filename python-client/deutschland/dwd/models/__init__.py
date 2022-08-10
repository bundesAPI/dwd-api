# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.dwd.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.dwd.model.crowd_meldung import CROWDMeldung
from deutschland.dwd.model.crowd_meldung_highest_severities_inner import (
    CROWDMeldungHighestSeveritiesInner,
)
from deutschland.dwd.model.crowd_meldung_meldungen_inner import (
    CROWDMeldungMeldungenInner,
)
from deutschland.dwd.model.error import Error
from deutschland.dwd.model.gemeinde_warnings import GemeindeWarnings
from deutschland.dwd.model.gemeinde_warnings_binnen_see import GemeindeWarningsBinnenSee
from deutschland.dwd.model.gemeinde_warnings_binnen_see209901000_inner import (
    GemeindeWarningsBinnenSee209901000Inner,
)
from deutschland.dwd.model.gemeinde_warnings_warnings_inner import (
    GemeindeWarningsWarningsInner,
)
from deutschland.dwd.model.station_overview import StationOverview
from deutschland.dwd.model.station_overview10865 import StationOverview10865
from deutschland.dwd.model.station_overview10865_days_inner import (
    StationOverview10865DaysInner,
)
from deutschland.dwd.model.station_overview10865_forecast1 import (
    StationOverview10865Forecast1,
)
from deutschland.dwd.model.station_overview10865_forecast2 import (
    StationOverview10865Forecast2,
)
from deutschland.dwd.model.station_overview_extended_get_station_ids_parameter_inner import (
    StationOverviewExtendedGetStationIdsParameterInner,
)
from deutschland.dwd.model.warning_coast import WarningCoast
from deutschland.dwd.model.warning_coast_warnings import WarningCoastWarnings
from deutschland.dwd.model.warning_coast_warnings501000007_inner import (
    WarningCoastWarnings501000007Inner,
)
from deutschland.dwd.model.warning_nowcast import WarningNowcast
from deutschland.dwd.model.warning_nowcast_warnings_inner import (
    WarningNowcastWarningsInner,
)
from deutschland.dwd.model.warning_nowcast_warnings_inner_regions_inner import (
    WarningNowcastWarningsInnerRegionsInner,
)
