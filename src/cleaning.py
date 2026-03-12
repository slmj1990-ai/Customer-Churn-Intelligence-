import pandas as pd
import numpy as np
import os


# ==============================
#  CONFIGURACION DE PATH 
# ==============================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_PATH = os.path.join(BASE_DIR, "data", "raw", "raw_dataset.csv")
PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed")


# ==============================
# CARGAR DATOS
# ==============================

def load_data(path):
    df = pd.read_csv(path)
    print("Dataset loaded successfully")
    print("Shape:", df.shape)
    return df


# ==============================
# ESTANDARIZAR NOMBRE DE COLUMNAS 
# ==============================

def standardize_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


# ================================
# INFORME DE CALIDAD DE LOS DATOS 
# ================================

def data_quality_report(df, stage="BEFORE CLEANING"):
    print(f"\n{'='*40}")
    print(f"DATA QUALITY REPORT - {stage}")
    print(f"{'='*40}")

    print("\nShape:", df.shape)

    print("\nTotal Missing Values:")
    print(df.isnull().sum().sum())

    print("\nTotal Duplicates:")
    print(df.duplicated().sum())

    print("\nData Types:")
    print(df.dtypes.value_counts())


# ==============================
# VARIABLES SEPARADAS
# ==============================

def separate_variables(df):
    numerical_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

    if "churned" in numerical_cols:
        numerical_cols.remove("churned")

    return numerical_cols, categorical_cols


# ==============================
# MANEJAR VALORES PERDIDOS 
# ==============================

def handle_missing_values(df, numerical_cols, categorical_cols):

    # Numéricas → mediana
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].median())

    # Categóricas → moda
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df


# ==============================
# ELIMINANDO DUPLICADOS 
# ==============================

def remove_duplicates(df):
    print("\nDuplicados encontrados:", df.duplicated().sum())
    df = df.drop_duplicates()
    return df


# ==============================
# OUTLIERS
# ==============================

def outlier_summary(df, numerical_cols):
    print("\n--- NUMERICAL SUMMARY (OUTLIER CHECK) ---")
    print(df[numerical_cols].describe())


# ==============================
# EJECUCION PRINCIPAL 
# ==============================

if __name__ == "__main__":

    # CARGAR DATOS
    df = load_data(RAW_PATH)
    df = standardize_columns(df)

    # ===== INFORME ANTES DE LA LIMPIEZA =====
    data_quality_report(df, stage="BEFORE CLEANING")

    # TIPO TARGET 
    if "churned" in df.columns:
        df["churned"] = df["churned"].astype(int)

    # SEPARANDO VARIABLES 
    numerical_cols, categorical_cols = separate_variables(df)

    # MANEJAR VALORES FALTANTES 
    df = handle_missing_values(df, numerical_cols, categorical_cols)

    # ELIMINANDO DUPLICADOS 
    df = remove_duplicates(df)

    # ===== INFROME DESPUES DE LA LIMPIEZA  =====
    data_quality_report(df, stage="AFTER CLEANING")

    outlier_summary(df, numerical_cols)

    print("\n Data cleaning comparison completed.")

    # CCREANDO FOLDER
    os.makedirs(PROCESSED_PATH, exist_ok=True)

    # SALVANDO DATASET LIMPIO
    cleaned_file_path = os.path.join(PROCESSED_PATH, "cleaned_dataset.csv")
    df.to_csv(cleaned_file_path, index=False)

    print(f"Cleaned dataset saved at: {cleaned_file_path}")
