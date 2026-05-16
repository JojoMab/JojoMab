import pandas as pd

from src.process_calculator import calculate_efficiency_percent, calculate_heat_transfer_rate, summarize_process


def test_heat_transfer_rate_is_positive_for_heated_flow():
    data = pd.DataFrame(
        {
            "flow_l_min": [12.0],
            "inlet_temp_c": [80.0],
            "outlet_temp_c": [120.0],
            "temperature_c": [180.0],
            "pressure_bar": [7.5],
        }
    )

    result = calculate_heat_transfer_rate(data)

    assert round(float(result.iloc[0]), 2) == 33.44


def test_efficiency_is_clipped_to_100_percent():
    data = pd.DataFrame(
        {
            "flow_l_min": [10.0],
            "inlet_temp_c": [20.0],
            "outlet_temp_c": [140.0],
        }
    )

    result = calculate_efficiency_percent(data)

    assert float(result.iloc[0]) == 100.0


def test_process_summary_contains_expected_keys():
    data = pd.DataFrame(
        {
            "temperature_c": [180.0, 190.0],
            "pressure_bar": [7.0, 8.0],
            "flow_l_min": [12.0, 14.0],
            "inlet_temp_c": [70.0, 75.0],
            "outlet_temp_c": [120.0, 130.0],
        }
    )

    summary = summarize_process(data)

    assert summary["measurement_count"] == 2
    assert summary["average_temperature_c"] == 185.0
    assert "average_heat_transfer_kw" in summary
    assert "average_efficiency_percent" in summary
