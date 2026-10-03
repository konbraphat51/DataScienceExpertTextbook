"""第1章：累積分布関数。左はサイコロの目（階段状）、右は f(x) = 2x の連続型（F(x) = x^2）。"""

import matplotlib.pyplot as plt
import numpy as np

from figstyle import COLORS, FULL_WIDTH, save, setup

setup()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(FULL_WIDTH, FULL_WIDTH * 0.36))

# 左：サイコロ。各段は [k, k+1) で一定（左端を含む●、右端を含まない○）
for k in range(0, 7):
    ax1.hlines(k / 6, k, k + 1, color=COLORS["main"])
    if k >= 1:
        ax1.plot(k, k / 6, "o", color=COLORS["main"], markersize=4)
        ax1.plot(k, (k - 1) / 6, "o", markerfacecolor="white", color=COLORS["main"], markersize=4)
ax1.hlines(0, -0.5, 0, color=COLORS["main"])
ax1.set_xlim(-0.5, 7)
ax1.set_yticks([0, 1 / 6, 2 / 6, 3 / 6, 4 / 6, 5 / 6, 1],
               ["0", "1/6", "2/6", "3/6", "4/6", "5/6", "1"])
ax1.set_xticks(range(0, 8))
ax1.set_xlabel("$x$")
ax1.set_ylabel("$F(x)$")
ax1.set_title("離散型（サイコロの目）")

# 右：F(x) = x^2 と f(x) = 2x
grid = np.linspace(-0.3, 1.3, 400)
F = np.clip(grid, 0, 1) ** 2
f = np.where((grid >= 0) & (grid <= 1), 2 * grid, 0)
ax2.plot(grid, f, color=COLORS["theorem"], linestyle="--", linewidth=1, label="$f(x)$（密度）")
ax2.plot(grid, F, color=COLORS["main"], label="$F(x)$")
ax2.set_xlabel("$x$")
ax2.set_title("連続型（$f(x) = 2x$）")
ax2.legend(frameon=False, loc="upper left")
ax2.set_ylim(0, 2.1)

fig.tight_layout()
save(fig, "prep_cdf")
