from kpis import KPIs
from currentkpis import CurrentKPIs
from forecastkpis import ForecastKPIs

# REport on current KPI values
kpis = KPIs()                          # Instantiate Subject
currentKPIs = CurrentKPIs(kpis)        # Instantiate Observer
forecastKPIs = ForecastKPIs(kpis)      # Instantiate Observer
kpis.set_kpis(25, 10, 5)
kpis.set_kpis(100, 50, 30)
kpis.set_kpis(50, 10, 20)

print('\n*** Detaching the currentKPIs observer.***\n\n')
kpis.detach(currentKPIs)
kpis.set_kpis(150, 110, 120)
