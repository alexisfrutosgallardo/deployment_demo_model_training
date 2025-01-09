from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline

def process_data(df: pd.DataFrame, columns_to_impute: list) -> pd.DataFrame:
    """
    Procesa los datos:
    - Imputa los valores faltantes
    - Escala las variables numéricas

    Args:
    - data (pd.DataFrame): DataFrame con los datos a procesar

    Returns:
    - pd.DataFrame: DataFrame con los datos procesados
    """

    # Imputa los valores faltantes
    #columns_to_impute
    # Creo un pipeline para imputar valores nulos con la media
    pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean', fill_value=None))])

    # Aplico el pipeline y lo redimensiono
    df['Income'] = pipeline.fit_transform(df['Income'].values.reshape(-1, 1))[:,0]

    return df