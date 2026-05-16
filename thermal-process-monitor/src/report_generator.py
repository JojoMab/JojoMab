from pathlib import Path


def build_report(process_summary: dict, alarm_summary: dict) -> str:
    """Build a readable process report from calculated summaries."""
    return f"""Prozessbericht - Thermal Process Monitor

Anzahl Messpunkte: {process_summary['measurement_count']}
Durchschnittstemperatur: {process_summary['average_temperature_c']} °C
Maximaltemperatur: {process_summary['max_temperature_c']} °C
Durchschnittsdruck: {process_summary['average_pressure_bar']} bar
Maximaldruck: {process_summary['max_pressure_bar']} bar
Durchschnittlicher Durchfluss: {process_summary['average_flow_l_min']} l/min
Durchschnittliche Wärmeübertragungsrate: {process_summary['average_heat_transfer_kw']} kW
Durchschnittlicher Anlagenwirkungsgrad: {process_summary['average_efficiency_percent']} %

Temperatur-Alarme: {alarm_summary['temperature_alarms']}
Druck-Alarme: {alarm_summary['pressure_alarms']}
Durchfluss-Alarme: {alarm_summary['flow_alarms']}
Messpunkte mit mindestens einem Alarm: {alarm_summary['alarm_rows']}

Alarmrate: {alarm_summary['alarm_rate_percent']} %
Bewertung: {alarm_summary['assessment']}
"""


def save_report(report: str, output_path: str | Path) -> None:
    """Save the generated report to disk."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report, encoding="utf-8")
