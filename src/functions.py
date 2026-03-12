
# ===============================
# IMPORTACIONES
# # ===============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    roc_curve,
    confusion_matrix
)

import shap


# ===============================
# ESCALADO DE CARACTERISTICAS 
# ===============================

def scale_numeric_features(df, target_column):

    scaler = StandardScaler()

    numeric_cols = df.select_dtypes(include=["int64","float64"]).columns

    if target_column in numeric_cols:
        numeric_cols = numeric_cols.drop(target_column)

    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df


# ===============================
# EVALUACION DEL MODELO 
# ===============================

def evaluate_model(model, X_test, y_test):

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:,1]

    accuracy = accuracy_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_prob)

    return accuracy, roc_auc


# ===============================
# COMPARACION DE MODELOS 
# ===============================

def model_comparison(results_dict):

    results_df = pd.DataFrame(results_dict).T
    results_df.columns = ["Accuracy","ROC-AUC"]

    return results_df


# ===============================
# CURVA ROC 
# ===============================

def plot_roc_curve(model, X_test, y_test):

    y_prob = model.predict_proba(X_test)[:,1]

    fpr, tpr, thresholds = roc_curve(y_test, y_prob)

    plt.figure(figsize=(8,6))

    plt.plot(fpr, tpr, label="Model")
    plt.plot([0,1],[0,1],'--')

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")

    plt.title("ROC Curve")

    plt.legend()

    plt.show()


# ===============================
# CONFUSION MATRIX
# ===============================

def plot_confusion_matrix(model, X_test, y_test):

    y_pred = model.predict(X_test)

    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6,5))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues"
    )

    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.title("Confusion Matrix")

    plt.show()


# ===================================
# IMPORTANCIA DE LAS CARACTERISTICAS 
# ===================================

def plot_feature_importance(model, X_train, top_n=15):

    feature_importance = pd.DataFrame({

        "feature": X_train.columns,
        "importance": model.feature_importances_

    })

    feature_importance = feature_importance.sort_values(
        "importance",
        ascending=False
    )

    top_features = feature_importance.head(top_n)

    plt.figure(figsize=(10,6))

    sns.barplot(
        data=top_features,
        x="importance",
        y="feature"
    )

    plt.title("Top Drivers of Churn")

    plt.show()


# ===============================
# EXPLICABILIDAD DE SHAP
# ===============================

def shap_analysis(model, X_train, X_test):

    explainer = shap.Explainer(model, X_train)

    shap_values = explainer(
        X_test,
        check_additivity=False
    )

    shap_values_class1 = shap_values[:,:,1]

    return shap_values_class1


def plot_shap_summary(shap_values):

    shap.plots.beeswarm(shap_values)


def plot_shap_importance(shap_values):

    shap.plots.bar(shap_values)


# ===============================
# PROBABILIDAD DE ABANDONO 
# ===============================

def create_prediction_dataframe(model, X_test, y_test):

    df_results = X_test.copy()

    df_results["churn_probability"] = model.predict_proba(X_test)[:,1]

    df_results["actual_churn"] = y_test.values

    return df_results


# ===============================
# SEGMENTACION DE RIESGOS 
# ===============================

def risk_segment(prob):

    if prob < 0.30:
        return "Low Risk"

    elif prob < 0.60:
        return "Medium Risk"

    else:
        return "High Risk"


def create_risk_segments(df):

    df["risk_segment"] = df["churn_probability"].apply(risk_segment)

    return df


# ===============================
# ESTRATEGIA DE RENTENCION 
# ===============================

def assign_retention_actions(df):

    retention_actions = {

        "Low Risk": "Loyalty Program",
        "Medium Risk": "Personalized Promotion",
        "High Risk": "Urgent Retention Campaign"
    }

    df["retention_action"] = df["risk_segment"].map(retention_actions)

    return df


# ===============================
# VISUALIZACION DE SEGMENTOS 
# ===============================

def plot_risk_segments(df):

    plt.figure(figsize=(8,5))

    sns.countplot(
        data=df,
        x="risk_segment",
        order=["Low Risk","Medium Risk","High Risk"]
    )

    plt.title("Customer Churn Risk Segments")

    plt.show()


def plot_probability_distribution(df):

    plt.figure(figsize=(8,5))

    sns.histplot(
        df["churn_probability"],
        bins=30
    )

    plt.title("Distribution of Churn Probability")

    plt.show()
