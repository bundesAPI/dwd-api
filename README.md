# dwd-api
API des Deutschen Wetterdienstes aus der DWD App.

## Einheiten

Im folgenden ist eine unvollständiger Tabelle mit ein paar Einheiten für die Werte, welche die DWD API zurückgibt. Sie wurde ermittelt durch ausprobieren und schauen was Sinn ergibt und dem entspricht, was die DWD App anzeigt. Wenn ihr mehr herausfindet, ergänzt die Tabelle bitte.

| Parameter     | Einheit | Kommentar                                                                                                            |
|---------------|---------|----------------------------------------------------------------------------------------------------------------------|
| `temperature` | 0.1 °C  | Temperatur in zehntel Grad Celisus                                                                                   |
| `start`       | ms      | [Unixzeit](https://de.wikipedia.org/wiki/Unixzeit) in Millisekunden, bei denen die Zeitreihe von Messwerten anfängt. |
| `timeStep`    | ms      | Zeitintervall zwischen den Messwerten einer Zeitreihe in Millisekunden.                                              |
