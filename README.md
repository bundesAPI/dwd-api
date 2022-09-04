# dwd-api
API des Deutschen Wetterdienstes (DWD) aus der DWD App.

Neben unterschiedlichen Wetterwarnungen (s.u.) lassen sich unter
/dwd.api.proxy.bund.dev/v30/stationOverviewExtended nach Angabe des Parameters *stationIDs*
auch die Wetterdaten ausgewählter Wetterstationen anfordern (wobei die sog. "Stationskennung" des DWD anzugeben ist). 

Die Liste der benötigten Stationskennungen kann z.B. [hier](https://www.dwd.de/DE/leistungen/klimadatendeutschland/stationsliste.html) recherchiert werden. Im HTML-Format findet sie sich [hier](https://www.dwd.de/DE/leistungen/klimadatendeutschland/statliste/statlex_html.html?view=nasPublication&nn=16102)

Unter [https://opendata.dwd.de/](https://opendata.dwd.de/) bietet der DWD darüber hinaus auch aktuelle und historische Daten zu diversen Wetter- und Kimaphänomenen zum Download an (vgl. hierzu die offizielle Dokumentation [hier](https://opendata.dwd.de/climate_environment/CDC/Readme_intro_CDC_ftp.pdf)). In diesem Zusammenhang erwähnenswert ist auch eine weitere offizielle Liste aller Wetterstationen (ohne Stationskennung aber mit sog. "Stations_id") [hier](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/recent/KL_Tageswerte_Beschreibung_Stationen.txt).


## Hinweis zu Einheiten

Im Folgenden ist eine unvollständige Tabelle angegeben, mit ein paar Einheiten für die Werte, welche die DWD API zurückgibt. Sie wurde ermittelt durch ausprobieren und schauen was Sinn ergibt und dem entspricht, was die DWD App anzeigt. Wenn ihr mehr herausfindet, ergänzt die Tabelle gerne.

| Parameter     | Einheit | Kommentar                                                                                                            |
|---------------|---------|----------------------------------------------------------------------------------------------------------------------|
| `temperature` | 0.1 °C  | Temperatur in zehntel Grad Celisus                                                                                   |
| `start`       | ms      | [Unixzeit](https://de.wikipedia.org/wiki/Unixzeit) in Millisekunden, bei denen die Zeitreihe von Messwerten anfängt. |
| `timeStep`    | ms      | Zeitintervall zwischen den Messwerten einer Zeitreihe in Millisekunden.                                              |


### Beispiele

```bash
weather=$(curl 'https://app-prod-ws.warnwetter.de/v30/stationOverviewExtended?stationIds=10865,G005')
crowdWarnings=$(curl 'https://s3.eu-central-1.amazonaws.com/app-prod-static.warnwetter.de/v16/crowd_meldungen_overview_v2.json')
nowcastWarnings=$(curl 'https://s3.eu-central-1.amazonaws.com/app-prod-static.warnwetter.de/v16/warnings_nowcast.json')
nowcastWarningsEnglish=$(curl 'https://s3.eu-central-1.amazonaws.com/app-prod-static.warnwetter.de/v16/warnings_nowcast_en.json')
gemeindeWarnings=$(curl 'https://s3.eu-central-1.amazonaws.com/app-prod-static.warnwetter.de/v16/gemeinde_warnings_v2.json')
gemeindeWarningsEnglish=$(curl 'https://s3.eu-central-1.amazonaws.com/app-prod-static.warnwetter.de/v16/gemeinde_warnings_v2_en.json')
coastWarnings=$(curl 'https://s3.eu-central-1.amazonaws.com/app-prod-static.warnwetter.de/v16/warnings_coast.json')
coastWarningsEnglish=$(curl 'https://s3.eu-central-1.amazonaws.com/app-prod-static.warnwetter.de/v16/warnings_coast_en.json')
seaWarnings=$(curl 'https://s3.eu-central-1.amazonaws.com/app-prod-static.warnwetter.de/v16/sea_warning_text.json')
alpsWeather=$(curl 'https://s3.eu-central-1.amazonaws.com/app-prod-static.warnwetter.de/v16/alpen_forecast_text_dwms.json')
avalancheWarnings=$(curl 'https://s3.eu-central-1.amazonaws.com/app-prod-static.warnwetter.de/v16/warnings_lawine.json')
```
