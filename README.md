# VancoSafe-PK: Clinical Decision Support Engine

## 🏥 The Problem: The Vancomycin Paradox
Vancomycin is a critical "last-line" antibiotic for MRSA, but it possesses a **Narrow Therapeutic Index**. 
* **The Stakes:** Over-dosing leads to permanent **Acute Kidney Injury (AKI)** in 10% of patients. 
* **The Complexity:** Standard linear dosing fails to account for fluctuating **Renal Clearance ($CrCl$)** in elderly or obese populations.

## 🚀 Project Overview
VancoSafe-PK is a hybrid software framework that combines **First-Principles Pharmacokinetics** with **Machine Learning** to provide a predictive "Safety Guard" for clinical dosing.

### Key Technical Pillars:
1. **Numerical ODE Solver:** Implements an Euler-method integration to solve the differential equation $dC/dt = -k_e \cdot C$, simulating drug accumulation over 72-hour multi-dose cycles.
2. **ML Safety Guard:** A Random Forest Classifier trained on 2,000 synthetic patient profiles to identify high-risk physiological patterns that lead to toxicity.
3. **Clinical Visualization:** Real-time serum concentration graphing with automated flagging of toxic troughs.

---

## 🛠️ Architecture

### 1. Physiological Engine (`core/physiology.py`)
Calculates the **Cockcroft-Gault** creatinine clearance and derives the elimination constant ($k_e$) and Volume of Distribution ($V_d$).

### 2. Numerical Simulator (`core/solver.py`)
Instead of static formulas, the engine uses a time-stepped simulation to account for multiple doses and drug "stacking" effects.


### 3. Predictive Analytics (`ml/guard.py`)
Uses `Scikit-Learn` to analyze the non-linear relationship between patient age, weight, and serum creatinine to predict AKI probability.




---

## 📊 Sample Output
When a dose is simulated for a high-risk patient (e.g., Age 80+, Creatinine > 2.0), the engine flags the simulation in **RED**, warning the clinician of a predicted "Toxic Trough."



---

## 💻 Installation & Usage

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/yourusername/VancoSafe-PK.git](https://github.com/yourusername/VancoSafe-PK.git)

2. **Install Dependancies**
pip install -r requirements.txt

3. **Run a Simulation**
 python main.py

 4. **The Final "Pro" Step: The `requirements.txt`**
Create a file named `requirements.txt` in the main folder and add this:
```text
numpy>=1.20.0
pandas>=1.3.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
