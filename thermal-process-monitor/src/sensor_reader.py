from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "timestamp",
    "temperature_c",
    "pressure_bar",
    "flow_l_min",
    "inlet_temp_c",
    "outlet_temp_c",
}


def load_sensor_data(csv_path: str | Path) -> pd.DataFrame:
    """Load sensor readings from a CSV file and parse timestamps."""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV-Datei nicht gefunden: {path}")

    data = pd.read_csv(path)
    if "timestamp" in data.columns:
        data["timestamp"] = pd.to_datetime(data["timestamp"], errors="raise")
    return data


def validate_sensor_data(data: pd.DataFrame) -> None:
    """Validate required columns, missing values and plausible physical ranges."""
    missing_columns = REQUIRED_COLUMNS.difference(data.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Fehlende Spalten: {missing}")

    if data.empty:
        raise ValueError("Die Sensordatei enthält keine Messpunkte.")

    if data[list(REQUIRED_COLUMNS)].isna().any().any():
        raise ValueError("Die Sensordaten enthalten fehlende Werte.")

    if (data["pressure_bar"] < 0).any():
        raise ValueError("Druckwerte dürfen nicht negativ sein.")

    if (data["flow_l_min"] < 0).any():
        raise ValueError("Durchflusswerte dürfen nicht negativ sein.")

    if (data["outlet_temp_c"] < data["inlet_temp_c"]).any():
        raise ValueError("Austrittstemperatur darf nicht unter Eintrittstemperatur liegen.")
