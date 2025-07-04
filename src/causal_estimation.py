import pandas as pd
import numpy as np
from dowhy import CausalModel
from load_and_clean import load_and_clean_data
import matplotlib.pyplot as plt
import os

def save_ate_plot(ate_value, control_mean, treated_mean):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    output_path = os.path.join(base_dir, 'outputs', 'results')
    os.makedirs(output_path, exist_ok=True)

    plt.figure(figsize=(6, 4))
    plt.bar(['Low NO₂ (Control)', 'High NO₂ (Treated)'], [control_mean, treated_mean], color=['skyblue', 'salmon'])
    plt.axhline(y=control_mean, linestyle='--', color='gray', label='Control Mean')
    plt.text(1, treated_mean + 1, f"ATE: {ate_value:.2f}", ha='center', color='black', fontsize=10)
    plt.title('Effect of High NO₂ on Relative Humidity (RH)')
    plt.ylabel('Relative Humidity')
    plt.tight_layout()

    save_path = os.path.join(output_path, 'ate_effect_plot.png')
    plt.savefig(save_path)
    plt.close()
    print(f"ATE plot saved to {save_path}")


def run_causal_estimation():
    df = load_and_clean_data()

    # create binary treatment variable based on NO2 threshold
    no2_threshold = df['NO2(GT)'].median()
    df['high_NO2'] = (df['NO2(GT)'] > no2_threshold).astype(int)

    # define treatment, outcome, and confounders
    treatment = 'high_NO2'
    outcome = 'RH'
    confounders = ['T', 'CO(GT)', 'NOx(GT)', 'C6H6(GT)']  # Add more if needed

    # create the causal model
    model = CausalModel(
        data=df,
        treatment=treatment,
        outcome=outcome,
        common_causes=confounders
    )

    # identify and estimate effect
    identified_estimand = model.identify_effect()
    estimate = model.estimate_effect(identified_estimand,
                                     method_name="backdoor.propensity_score_matching")

    # printing the results
    print("Estimated Causal Effect (ATE):", estimate.value)

    # Plot results
    treated_mean = df.loc[df[treatment] == 1, outcome].mean()
    control_mean = df.loc[df[treatment] == 0, outcome].mean()
    save_ate_plot(estimate.value, control_mean, treated_mean)


    refutation = model.refute_estimate(identified_estimand, estimate, method_name="placebo_treatment_refuter")
    print("\nRefutation Result:")
    print(refutation)

if __name__ == "__main__":
    run_causal_estimation()
