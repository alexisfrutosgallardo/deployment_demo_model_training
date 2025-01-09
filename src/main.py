import sys, os

# Agregar la raiz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..") ))

from src.data.data_loader import load_data
from src.data.data_processor import process_data

def main():
    print("Comienza a correr el entrenamiento")
    # Carga los datos
    data = load_data(file_path="data/raw/marketing_campaign.csv")
    print(data.head(2))

    # Procesa los datos
    #process_data =  process_data(df=data, columns_to_impute=['Income'])

if __name__ == "__main__":
    main()