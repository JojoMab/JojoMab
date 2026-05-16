from pathlib import Path

from src.alarm_handler import evaluate_alarms, summarize_alarms
from src.process_calculator import summarize_process
from src.report_generator import build_report, save_report
from src.sensor_reader import load_sensor_data, validate_sensor_data


DATA_PATH = Path("data/sensor_readings.csv")
REPORT_PATH = Path("reports/process_report.txt")


def main() -> None:
    print("Lade Sensordaten...", end=" ")
    sensor_data = load_sensor_data(DATA_PATH)
    validate_sensor_data(sensor_data)
    print(f"{len(sensor_data)} Messpunkte geladen.")

    print("Prüfe Grenzwerte...")
    evaluated_data = evaluate_alarms(sensor_data)
    process_summary = summarize_process(evaluated_data)
    alarm_summary = summarize_alarms(evaluated_data)

    report = build_report(process_summary, alarm_summary)
    save_report(report, REPORT_PATH)

    print(f"\nTemperatur-Alarme:  {alarm_summary['temperature_alarms']}")
    print(f"Druck-Alarme:       {alarm_summary['pressure_alarms']}")
    print(f"Durchfluss-Alarme:  {alarm_summary['flow_alarms']}")
    print(f"Alarmrate:          {alarm_summary['alarm_rate_percent']:.1f} %")
    print(f"\nBericht gespeichert: {REPORT_PATH}")
    print(f"Bewertung: {alarm_summary['assessment']}")


if __name__ == "__main__":
    main()
