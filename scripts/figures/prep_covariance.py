"""第1章：共分散の符号のイメージ（平均で区切った 4 つの領域と、偏差の積の符号）。"""

import numpy as np
from matplotlib.patches import Rectangle

from figstyle import COLORS, new_figure, save

hours = np.array([1, 2, 3, 4, 5])
score = np.array([50, 60, 55, 75, 80])
mx, my = hours.mean(), score.mean()

fig, ax = new_figure(aspect=0.62)
ax.axvline(mx, color=COLORS["ref"], linestyle="--", linewidth=1)
ax.axhline(my, color=COLORS["ref"], linestyle="--", linewidth=1)

# 各点の偏差の積を長方形で示す（正：緑、負：橙）
for x, y in zip(hours, score):
    prod = (x - mx) * (y - my)
    if prod == 0:
        continue
    color = COLORS["merit"] if prod > 0 else COLORS["theorem"]
    ax.add_patch(Rectangle((min(x, mx), min(y, my)), abs(x - mx), abs(y - my),
                           facecolor=color, alpha=0.15, edgecolor="none"))
ax.scatter(hours, score, color=COLORS["main"], zorder=3)

kw = {"fontsize": 9, "ha": "center", "va": "center", "fontweight": "bold"}
ax.text(4.6, 85, "積が正", color=COLORS["merit"], **kw)
ax.text(1.4, 47, "積が正", color=COLORS["merit"], **kw)
ax.text(1.4, 85, "積が負", color=COLORS["theorem"], **kw)
ax.text(4.6, 47, "積が負", color=COLORS["theorem"], **kw)
ax.annotate(r"$\bar{x}=3$", (mx, 42), xytext=(mx + 0.08, 42), fontsize=8, color=COLORS["ref"])
ax.annotate(r"$\bar{y}=64$", (0.55, my), xytext=(0.55, my + 1), fontsize=8, color=COLORS["ref"])

ax.set_xlim(0.5, 5.5)
ax.set_ylim(40, 90)
ax.set_xlabel("勉強時間 $x$（時間）")
ax.set_ylabel("点数 $y$")

save(fig, "prep_covariance")
