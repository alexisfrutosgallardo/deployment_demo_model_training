# deployment_demo_model_training
Este es un demo que fue hecho para lanzar un simple modelo de machine learning como ejemplo para enseñar a estudiantes a usar el open source

model_training/
|-- src/
    |-- data/
        |-- data_loader.py      # Carga de datos
        |-- data_splitter.py    # División de datos
        |-- data_processor.py   # Procesamiento de datos
    |-- model/
        |-- model/
        |   |-- trainer.py      # Entrenamiento del modelo
        |   |-- evaluator.py    # Evaluación del modelo
        |   |-- saver.py        # Guardado del modelo
        |-- main.py             # Orquestación del entrenamiento
|-- data/
    |-- marketing_campaign.csv  # Dataset de Customer Personality Analysis
|-- models/
    |-- trained_model.pkl       # Modelo entrenado (generado tras el entrenamiento)
|-- requirements.txt            # Dependencias necesarias
