from kpis import KPIs
from currentkpis import CurrentKPIs
from forecastkpis import ForecastKPIs

# Report on current KPI values
# kpis = KPIs()                          # Instantiate Subject
# currentKPIs = CurrentKPIs(kpis)        # Instantiate Observer
# forecastKPIs = ForecastKPIs(kpis)      # Instantiate Observer
with KPIs() as kpis:
    with CurrentKPIs(kpis), ForecastKPIs(kpis):
        kpis.set_kpis(25, 10, 5)
        kpis.set_kpis(100, 50, 30)
        kpis.set_kpis(50, 10, 20)

# print('\n*** Detaching the currentKPIs observer.***\n\n')
# kpis.detach(currentKPIs)

print('\n***Exited context managers.***\n')
kpis.set_kpis(150, 110, 120)
