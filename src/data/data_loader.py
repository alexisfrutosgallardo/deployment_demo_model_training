import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Carga los datos de un archivo CSV en un DataFrame de pandas.

    Args:
        file_path (str): Ruta del archivo CSV a cargar.

    Returns:
        pd.DataFrame: DataFrame con los datos del archivo CSV.
    """
    return pd.read_csv(file_path)