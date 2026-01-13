class RenalPhysiology:
    @staticmethod
    def cockcroft_gault(age, weight, creatinine, is_male=True):
        """Calculates Creatinine Clearance (CrCl) in mL/min."""
        modifier = 1.0 if is_male else 0.85
        crcl = ((140 - age) * weight * modifier) / (72 * creatinine)
        return max(crcl, 1.0) # Prevent division by zero

    @staticmethod
    def get_pk_params(crcl, weight):
        """Derives Pharmacokinetic constants from renal function."""
        # ke (elimination constant) and Vd (volume of distribution)
        ke = 0.00083 * crcl + 0.0044
        vd = 0.7 * weight
        return ke, vd