import pandas as pd

from src.alarm_handler import evaluate_alarms, summarize_alarms


def test_evaluate_alarms_detects_temperature_alarm():
    data = pd.DataFrame(
        {
            "temperature_c": [251.0],
            "pressure_bar": [8.0],
            "flow_l_min": [12.0],
        }
    )

    result = evaluate_alarms(data)

    assert bool(result.loc[0, "temperature_alarm"]) is True
    assert bool(result.loc[0, "any_alarm"]) is True


def test_evaluate_alarms_detects_pressure_alarm():
    data = pd.DataFrame(
        {
            "temperature_c": [180.0],
            "pressure_bar": [10.5],
            "flow_l_min": [12.0],
        }
    )

    result = evaluate_alarms(data)

    assert bool(result.loc[0, "pressure_alarm"]) is True
    assert bool(result.loc[0, "any_alarm"]) is True


def test_evaluate_alarms_detects_low_flow_alarm():
    data = pd.DataFrame(
        {
            "temperature_c": [180.0],
            "pressure_bar": [8.0],
            "flow_l_min": [7.5],
        }
    )

    result = evaluate_alarms(data)

    assert bool(result.loc[0, "flow_alarm"]) is True
    assert bool(result.loc[0, "any_alarm"]) is True


def test_alarm_summary_calculates_alarm_rate():
    data = pd.DataFrame(
        {
            "temperature_c": [180.0, 251.0],
            "pressure_bar": [8.0, 8.0],
            "flow_l_min": [12.0, 12.0],
        }
    )

    evaluated = evaluate_alarms(data)
    summary = summarize_alarms(evaluated)

    assert summary["temperature_alarms"] == 1
    assert summary["alarm_rows"] == 1
    assert summary["alarm_rate_percent"] == 50.0
