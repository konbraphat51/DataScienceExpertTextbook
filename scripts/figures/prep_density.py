"""第1章：ヒストグラムから確率密度関数へ（左）と「面積が確率」（右）。

例として、確率密度関数 f(x) = 2x（0 <= x <= 1）の確率変数を使う。
"""

import matplotlib.pyplot as plt
import numpy as np

from figstyle import COLORS, FULL_WIDTH, save, setup

rng = np.random.default_rng(seed=0)
x = np.sqrt(rng.random(10000))  # f(x) = 2x にしたがう乱数（累積分布関数 x^2 の逆関数を使う）
grid = np.linspace(0, 1, 200)

setup()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(FULL_WIDTH, FULL_WIDTH * 0.36))

# 左：棒の面積が相対度数になるヒストグラム（density=True）
ax1.hist(x[:200], bins=5, range=(0, 1), density=True, color=COLORS["main"], alpha=0.25,
         edgecolor=COLORS["main"], label="200 個・5 階級")
ax1.hist(x, bins=40, range=(0, 1), density=True, histtype="step", color=COLORS["merit"],
         label="10000 個・40 階級")
ax1.plot(grid, 2 * grid, color=COLORS["theorem"], label="$f(x) = 2x$")
ax1.set_xlabel("$x$")
ax1.set_ylabel("相対度数 ÷ 階級の幅")
ax1.set_title("ヒストグラムを細かくすると曲線に近づく")
ax1.legend(frameon=False, loc="upper left")
ax1.set_ylim(0, 2.6)

# 右：P(0.5 <= X <= 1) は x = 0.5 から 1 までの面積
ax2.plot(grid, 2 * grid, color=COLORS["theorem"])
mask = grid >= 0.5
ax2.fill_between(grid[mask], 2 * grid[mask], color=COLORS["theorem"], alpha=0.2)
ax2.text(0.76, 0.55, "面積 $= 0.75$\n$= P(0.5 \\leq X \\leq 1)$", ha="center", fontsize=8)
ax2.set_xlabel("$x$")
ax2.set_ylabel("$f(x)$")
ax2.set_title("確率は面積で表される")
ax2.set_xlim(-0.05, 1.05)
ax2.set_ylim(0, 2.6)

fig.tight_layout()
save(fig, "prep_density")
