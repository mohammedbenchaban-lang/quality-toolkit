# Quality Toolkit

A lightweight Python toolkit that turns classic Quality Management methods into reusable, scriptable tools:

- **FMEA Risk Ranking** - calculate Risk Priority Number (Severity x Occurrence x Detection) and auto-rank failure modes
- **Pareto Chart Generator** - turns defect counts into a bar + cumulative % chart (80/20 line included)
- **5-Why Logger** - structured root-cause tracking down to a final answer

Built from real coursework applying FMEA, Pareto-Lorenz, and 5-Why analysis to a ceramic mug production line, turned into a general-purpose tool anyone can reuse for their own process.

## Install

```bash
pip install -r requirements.txt
```

## Usage

```python
from quality_toolkit import FMEAItem, print_fmea_table, pareto_chart, FiveWhy

items = [
    FMEAItem("Kiln temperature drift", severity=8, occurrence=4, detection=5),
    FMEAItem("Glaze thickness inconsistency", severity=6, occurrence=6, detection=4),
]
print_fmea_table(items)

pareto_chart(["Glaze defects", "Cracks", "Warping"], [42, 25, 15])

five_why = FiveWhy(problem="Cracks near the handle")
five_why.add_why("Weak clay-glaze bond at the joint")
print(five_why.report())
```

Run the full walkthrough:

```bash
python example.py
```

Running `example.py` ranks failure modes by risk, generates `pareto.png` in your working directory, and prints a full 5-Why trace.

## Built With

- Python 3
- Matplotlib

## Author

**Mohammed Chems Eddine Benchabane** - Materials Design and Logistics student, Czestochowa University of Technology
