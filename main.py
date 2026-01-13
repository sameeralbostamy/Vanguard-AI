import matplotlib.pyplot as plt
from core.physiology import RenalPhysiology
from core.solver import PKSolver
from ml.guard import AKIGuard

def run_simulation(age, weight, creat, dose_mg):
    # 1. Setup ML Safety Guard
    guard = AKIGuard()
    guard.train_on_synthetic_data()
    risk = guard.predict_risk(age, weight, creat, dose_mg)

    # 2. Setup Physics/Bio Math
    crcl = RenalPhysiology.cockcroft_gault(age, weight, creat)
    ke, vd = RenalPhysiology.get_pk_params(crcl, weight)
    
    # 3. Solve Simulation
    solver = PKSolver(ke, vd)
    t, c = solver.simulate_multidose(dose_mg, interval_hrs=12, total_hrs=48)

    # 4. Plot Results
    plt.style.use('ggplot')
    plt.figure(figsize=(10, 5))
    color = 'red' if risk > 0.5 else 'blue'
    
    plt.plot(t, c, color=color, label=f"Serum Level (Risk: {risk:.1%})")
    plt.axhspan(15, 20, color='green', alpha=0.2, label='Safe Zone')
    plt.title(f"Vancomycin Accumulation Simulation (Patient CrCl: {crcl:.1f} mL/min)")
    plt.ylabel("Concentration (mg/L)")
    plt.xlabel("Time (Hours)")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Test: Elderly patient with moderate kidney impairment
    run_simulation(age=78, weight=70, creat=1.9, dose_mg=1000)