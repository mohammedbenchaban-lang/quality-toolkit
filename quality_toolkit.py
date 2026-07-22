"""
Quality Toolkit
================
A small Python toolkit for common Quality Management analyses:
FMEA (Risk Priority Number), Pareto chart generation, and a
guided 5-Why root-cause logger.

Usage examples are in example.py
"""

from dataclasses import dataclass, field
from typing import List
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# FMEA
# ---------------------------------------------------------------------------

@dataclass
class FMEAItem:
    failure_mode: str
    severity: int      # 1-10
    occurrence: int    # 1-10
    detection: int     # 1-10

    @property
    def rpn(self) -> int:
        """Risk Priority Number = Severity x Occurrence x Detection"""
        return self.severity * self.occurrence * self.detection


def rank_fmea(items: List[FMEAItem]) -> List[FMEAItem]:
    """Return FMEA items sorted by RPN, highest risk first."""
    return sorted(items, key=lambda i: i.rpn, reverse=True)


def print_fmea_table(items: List[FMEAItem]) -> None:
    ranked = rank_fmea(items)
    print(f"{'Failure Mode':<30}{'Sev':>5}{'Occ':>5}{'Det':>5}{'RPN':>7}")
    print("-" * 52)
    for item in ranked:
        print(f"{item.failure_mode:<30}{item.severity:>5}{item.occurrence:>5}"
              f"{item.detection:>5}{item.rpn:>7}")


# ---------------------------------------------------------------------------
# Pareto Chart
# ---------------------------------------------------------------------------

def pareto_chart(categories: List[str], counts: List[int],
                  title: str = "Pareto Chart", save_path: str = "pareto.png") -> str:
    """Generate a Pareto chart (bars + cumulative % line) and save as PNG."""
    paired = sorted(zip(categories, counts), key=lambda x: x[1], reverse=True)
    categories, counts = zip(*paired)
    total = sum(counts)
    cumulative = []
    running = 0
    for c in counts:
        running += c
        cumulative.append(running / total * 100)

    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax1.bar(categories, counts, color="#2E9EF7")
    ax1.set_ylabel("Defect Count")
    ax1.set_xlabel("Defect Category")
    plt.xticks(rotation=30, ha="right")

    ax2 = ax1.twinx()
    ax2.plot(categories, cumulative, color="#E63946", marker="o")
    ax2.axhline(80, color="gray", linestyle="--", linewidth=1)
    ax2.set_ylabel("Cumulative %")
    ax2.set_ylim(0, 110)

    plt.title(title)
    fig.tight_layout()
    fig.savefig(save_path, dpi=150)
    plt.close(fig)
    return save_path


# ---------------------------------------------------------------------------
# 5-Why
# ---------------------------------------------------------------------------

@dataclass
class FiveWhy:
    problem: str
    whys: List[str] = field(default_factory=list)

    def add_why(self, answer: str) -> None:
        if len(self.whys) >= 5:
            raise ValueError("5-Why analysis already has 5 answers")
        self.whys.append(answer)

    def report(self) -> str:
        lines = [f"Problem: {self.problem}"]
        for i, why in enumerate(self.whys, start=1):
            lines.append(f"  Why #{i}: {why}")
        if self.whys:
            lines.append(f"\nRoot cause (final why): {self.whys[-1]}")
        return "\n".join(lines)
