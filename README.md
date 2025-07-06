# Pollution-Causal-Inference

This project investigates **causal relationships** between air pollutants and environmental conditions using the [UCI Air Quality dataset](https://archive.ics.uci.edu/ml/datasets/Air+Quality). Specifically, we focus on **estimating the causal effect of NO₂ on Relative Humidity (RH)** using the [DoWhy](https://github.com/py-why/dowhy) library.

---

## Dataset

- **Source**: UCI Air Quality dataset  
- **File used**: `AirQualityUCI.xlsx`  
- **Features include**: NO₂ (NO2(GT)), CO (CO(GT)), C6H6, NOx, RH (Relative Humidity), Temperature, etc.  
- **Granularity**: Hourly readings across several months

---

## 🔍 Exploratory Data Analysis

Visualizations generated from `src/exploratory_analysis.py` help explore distributions, time series trends, and correlations.

### Time Series and Distribution Plots

| Pollutant        | Time Series                                   | Distribution                                  |
|------------------|-----------------------------------------------|-----------------------------------------------|
| NO₂              | ![NO2_TS](outputs/figures/NO2GT_timeseries.png) | ![NO2_Dist](outputs/figures/NO2GT_distribution.png) |
| CO               | ![CO_TS](outputs/figures/COGT_timeseries.png)  | ![CO_Dist](outputs/figures/COGT_distribution.png)  |
| NOx              | ![NOx_TS](outputs/figures/NOxGT_timeseries.png) | ![NOx_Dist](outputs/figures/NOxGT_distribution.png) |
| C6H6             | ![C6H6_TS](outputs/figures/C6H6GT_timeseries.png) | ![C6H6_Dist](outputs/figures/C6H6GT_distribution.png) |

### Correlation Matrix
<div align="center">
<img src="outputs/figures/correlation_matrix.png" alt="Correlation Matrix" width="500"/>
</div>

---

## 🔁 Causal Question

**What is the causal effect of NO₂ (NO2(GT)) on Relative Humidity (RH)?**

---

## Causal Graph (DAG)

We model assumed causal dependencies using a Directed Acyclic Graph (DAG):

<div align="center">
<img src="outputs/figures/causal_dag.png" alt="ATE Plot" width="400"/>
</div>

---

## 📈 Estimation and Refutation

Using DoWhy, we estimated the **Average Treatment Effect (ATE)** and validated our findings with a placebo test.

### ➕ Estimated Effect

- **ATE (Average Treatment Effect)** = **-15.83**
- This implies that high NO₂ concentrations cause an estimated **15.83 unit decrease in Relative Humidity (RH)**.

### ❓ Refutation Test

We applied a placebo treatment test to validate the robustness of the estimated effect:

- **Original Effect**: -15.83  
- **Placebo Effect**: -0.04  
- **p-value**: 0.9 (indicating no significant spurious effect)

---

## 📉 Final Visual Result

A clear illustration of the effect:

<div align="center">
<img src="outputs/results/ate_effect_plot.png" alt="ATE Plot" width="400"/>
</div>

