import pandas as pd


TEMPERATURE_LIMIT_C = 250.0
PRESSURE_LIMIT_BAR = 10.0
MIN_FLOW_L_MIN = 8.0


def evaluate_alarms(data: pd.DataFrame) -> pd.DataFrame:
    """Add alarm columns for all monitored process values."""
    result = data.copy()
    result["temperature_alarm"] = result["temperature_c"] > TEMPERATURE_LIMIT_C
    result["pressure_alarm"] = result["pressure_bar"] > PRESSURE_LIMIT_BAR
    result["flow_alarm"] = result["flow_l_min"] < MIN_FLOW_L_MIN
    result["any_alarm"] = result[
        ["temperature_alarm", "pressure_alarm", "flow_alarm"]
    ].any(axis=1)
    return result


def summarize_alarms(data: pd.DataFrame) -> dict[str, int | float | str]:
    """Summarize alarm counts and create a short assessment."""
    measurement_count = int(len(data))
    temperature_alarms = int(data["temperature_alarm"].sum())
    pressure_alarms = int(data["pressure_alarm"].sum())
    flow_alarms = int(data["flow_alarm"].sum())
    alarm_rows = int(data["any_alarm"].sum())
    alarm_rate_percent = round((alarm_rows / measurement_count) * 100, 1) if measurement_count else 0.0

    if alarm_rate_percent == 0:
        assessment = "Stabiler Anlagenzustand. Keine Alarme erkannt."
    elif alarm_rate_percent < 10:
        assessment = "Leichte Auffälligkeiten. Weitere Beobachtung empfohlen."
    else:
        assessment = "Erhöhte Alarmrate. Überprüfung empfohlen."

    return {
        "measurement_count": measurement_count,
        "temperature_alarms": temperature_alarms,
        "pressure_alarms": pressure_alarms,
        "flow_alarms": flow_alarms,
        "alarm_rows": alarm_rows,
        "alarm_rate_percent": alarm_rate_percent,
        "assessment": assessment,
    }
