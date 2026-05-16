import numpy as np
import pandas as pd


def calculate_heat_transfer_rate(data: pd.DataFrame) -> pd.Series:
    """
    Calculate an approximate heat transfer rate in kW.

    Simplified assumption:
    - medium behaves like water
    - density approximately 1 kg/l
    - specific heat capacity approximately 4.18 kJ/(kg*K)
    """
    mass_flow_kg_s = data["flow_l_min"] / 60.0
    delta_t_k = data["outlet_temp_c"] - data["inlet_temp_c"]
    specific_heat_kj_kg_k = 4.18
    return mass_flow_kg_s * specific_heat_kj_kg_k * delta_t_k


def calculate_efficiency_percent(data: pd.DataFrame, target_delta_t: float = 80.0) -> pd.Series:
    """Calculate a simplified plant efficiency based on the achieved temperature difference."""
    delta_t = data["outlet_temp_c"] - data["inlet_temp_c"]
    efficiency = (delta_t / target_delta_t) * 100.0
    return pd.Series(np.clip(efficiency, 0, 100), index=data.index)


def summarize_process(data: pd.DataFrame) -> dict[str, float | int]:
    """Create a compact summary of relevant process values."""
    heat_transfer_kw = calculate_heat_transfer_rate(data)
    efficiency_percent = calculate_efficiency_percent(data)

    return {
        "measurement_count": int(len(data)),
        "average_temperature_c": round(float(data["temperature_c"].mean()), 2),
        "max_temperature_c": round(float(data["temperature_c"].max()), 2),
        "average_pressure_bar": round(float(data["pressure_bar"].mean()), 2),
        "max_pressure_bar": round(float(data["pressure_bar"].max()), 2),
        "average_flow_l_min": round(float(data["flow_l_min"].mean()), 2),
        "average_heat_transfer_kw": round(float(heat_transfer_kw.mean()), 2),
        "average_efficiency_percent": round(float(efficiency_percent.mean()), 2),
    }
