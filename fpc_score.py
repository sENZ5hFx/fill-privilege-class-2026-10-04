"""Fill-Privilege Class scorer. Dual of ANC. Not a physical discovery."""

from __future__ import annotations


def fpc_score(fill_as_fact: float, evidence: float, spoken: float, prior_overlap: float) -> float:
    fill = min(1.0, max(0.0, fill_as_fact))
    ev = min(1.0, max(0.0, evidence))
    sp = min(1.0, max(0.0, spoken))
    ov = min(1.0, max(0.0, prior_overlap))
    return round(40 * fill * ev * (1 - sp) * (1 - ov), 4)


if __name__ == "__main__":
    rows = [
        ("climate_reanalysis_surrogate", 1, 0.91, 0.46, 0.30),
        ("tropical_csr_imputed_traits", 1, 0.86, 0.50, 0.26),
        ("ukb_hardcall", 1, 0.80, 0.64, 0.38),
        ("marine_sdm_pseudoabsence", 0.75, 0.68, 0.48, 0.42),
        ("photo_z_estimand", 0.12, 0.70, 0.90, 0.70),
        ("pop_gwas_kill", 0.05, 0.90, 0.88, 0.55),
    ]
    for name, *args in rows:
        print(f"{name:36} {fpc_score(*args):8.4f}")
