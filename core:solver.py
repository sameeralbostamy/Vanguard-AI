import numpy as np

class PKSolver:
    def __init__(self, ke, vd):
        self.ke = ke
        self.vd = vd

    def simulate_multidose(self, dose_mg, interval_hrs, total_hrs, dt=0.01):
        """
        Solves dC/dt = -ke * C numerically.
        Allows for drug accumulation over multiple doses.
        """
        steps = int(total_hrs / dt)
        times = np.linspace(0, total_hrs, steps)
        concentrations = np.zeros(steps)
        current_c = 0

        for i, t in enumerate(times):
            # Administer new dose at every interval
            if i > 0 and (t % interval_hrs) < dt:
                current_c += (dose_mg / self.vd)
            
            # ODE: ΔC = (-ke * C) * Δt
            delta_c = -self.ke * current_c * dt
            current_c += delta_c
            concentrations[i] = current_c

        return times, concentrations