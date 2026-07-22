"""
Example: applying the Quality Toolkit to a ceramic mug production line.
Run: python example.py
"""

from quality_toolkit import FMEAItem, print_fmea_table, pareto_chart, FiveWhy

# --- FMEA -------------------------------------------------------------
items = [
    FMEAItem("Kiln temperature drift", severity=8, occurrence=4, detection=5),
    FMEAItem("Glaze thickness inconsistency", severity=6, occurrence=6, detection=4),
    FMEAItem("Handle attachment crack", severity=9, occurrence=3, detection=6),
    FMEAItem("Mold surface defect", severity=5, occurrence=5, detection=3),
]

print("=== FMEA Ranking (highest risk first) ===")
print_fmea_table(items)

# --- Pareto -------------------------------------------------------------
categories = ["Glaze defects", "Cracks", "Warping", "Chipping", "Color mismatch"]
counts = [42, 25, 15, 10, 8]

path = pareto_chart(categories, counts, title="Ceramic Mug Defects - Pareto Chart")
print(f"\nPareto chart saved to: {path}")

# --- 5-Why ---------------------------------------------------------------
five_why = FiveWhy(problem="Cracks appear near the mug handle")
five_why.add_why("The clay-glaze bond is weak at the joint")
five_why.add_why("Glaze was applied before the joint fully dried")
five_why.add_why("Drying schedule was not followed for handle-attached pieces")
five_why.add_why("No separate drying checklist exists for handled ware")
five_why.add_why("Process documentation wasn't updated after handle attachment was introduced")

print("\n=== 5-Why Analysis ===")
print(five_why.report())
