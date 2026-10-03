"""標準正規分布表（上側確率 Q(z) = P(Z >= z)）を TeX の表として書き出す。

    uv run scripts/tables/normal_table.py   → tex/tables/normal-upper.tex

行が z の小数第 1 位まで、列が小数第 2 位。本文では \\input{tables/normal-upper} で読み込む。
"""

from pathlib import Path

from scipy import stats

OUT = Path(__file__).resolve().parents[2] / "tex" / "tables" / "normal-upper.tex"


def fmt(q: float) -> str:
    """小数第 4 位まで。0.0005 未満になる所は有効数字 3 桁で書く。"""
    if q >= 0.0005:
        return f".{round(q * 10000):04d}"
    return f"{q:.2e}".replace("e-0", r"\times10^{-") + "}"


lines = [
    "% このファイルは scripts/tables/normal_table.py で作る。直接編集しない。",
    r"\begin{tabular}{c|*{10}{c}}",
    r"  \toprule",
    "  $z$ & " + " & ".join(f".{j:02d}" for j in range(10)) + r" \\",
    r"  \midrule",
]
for i in range(31):
    z0 = i / 10
    cells = [fmt(stats.norm.sf(z0 + j / 100)) for j in range(10)]
    cells = [c if c.startswith(".") else f"${c}$" for c in cells]
    lines.append(f"  {z0:.1f} & " + " & ".join(cells) + r" \\")
    if i % 5 == 4 and i != 30:
        lines.append(r"  \addlinespace[2pt]")
lines += [r"  \bottomrule", r"\end{tabular}", ""]

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"saved: {OUT.relative_to(OUT.parents[2])}")
