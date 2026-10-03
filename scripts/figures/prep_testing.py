"""第1章：仮説検定の図（3 つ）。

- prep_rejection：両側検定の棄却域と、観測値 z = 2.4、p 値
- prep_power：帰無仮説（μ=100）と対立仮説（μ=101）のもとでの標本平均の分布。α、β、検出力
- prep_one_two_sided：両側検定と片側検定の棄却域
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from figstyle import COLORS, FULL_WIDTH, WIDTH, new_figure, save, setup

z = np.linspace(-4, 4, 500)
phi = stats.norm.pdf(z)

# ---------------------------------------------------------------- 棄却域と p 値
fig, ax = new_figure(WIDTH, aspect=0.45)
ax.plot(z, phi, color=COLORS["main"])
for side in (z >= 1.96, z <= -1.96):
    ax.fill_between(z[side], phi[side], color=COLORS["theorem"], alpha=0.25, linewidth=0)
for side in (z >= 2.4, z <= -2.4):
    ax.fill_between(z[side], phi[side], color=COLORS["theorem"], alpha=0.7, linewidth=0)
ax.axvline(2.4, color=COLORS["merit"], linewidth=1.2)
ax.annotate("観測値 $z = 2.4$", xy=(2.4, 0.2), xytext=(2.55, 0.25), fontsize=8,
            color=COLORS["merit"])
ax.annotate("棄却域（$|Z| \\geq 1.96$）\n両側で面積 0.05", xy=(-2.3, 0.02), xytext=(-4, 0.22),
            fontsize=8, color=COLORS["theorem"],
            arrowprops={"arrowstyle": "->", "color": COLORS["theorem"]})
ax.annotate("濃い部分の面積 = p 値", xy=(2.7, 0.005), xytext=(2.3, 0.12), fontsize=8,
            color=COLORS["theorem"],
            arrowprops={"arrowstyle": "->", "color": COLORS["theorem"]})
ax.set_xticks([-1.96, 0, 1.96], ["$-1.96$", "0", "$1.96$"])
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.set_xlabel("検定統計量 $Z$（帰無仮説のもとで $\\mathrm{N}(0,1)$）")
save(fig, "prep_rejection")

# ---------------------------------------------------------------- 検出力
se = 0.5
x = np.linspace(98, 103.2, 600)
f0 = stats.norm.pdf(x, 100, se)
f1 = stats.norm.pdf(x, 101, se)
lo, hi = 100 - 1.96 * se, 100 + 1.96 * se

fig, ax = new_figure(FULL_WIDTH * 0.85, aspect=0.42)
ax.plot(x, f0, color=COLORS["main"], label="帰無仮説 $\\mu = 100$ のもとでの $\\bar{X}$ の分布")
ax.plot(x, f1, color=COLORS["merit"], label="本当は $\\mu = 101$ のときの $\\bar{X}$ の分布")
m = x >= hi
ax.fill_between(x[m], f1[m], color=COLORS["merit"], alpha=0.25, linewidth=0, label="検出力 $1-\\beta$")
m = x < hi
ax.fill_between(x[m], f1[m], color=COLORS["ref"], alpha=0.25, linewidth=0, hatch="///",
                label="第 2 種の過誤の確率 $\\beta$")
for side in (x >= hi, x <= lo):
    ax.fill_between(x[side], f0[side], color=COLORS["theorem"], alpha=0.6, linewidth=0)
ax.fill_between([], [], color=COLORS["theorem"], alpha=0.6, label="第 1 種の過誤の確率 $\\alpha$")
ax.axvline(hi, color=COLORS["example"], linestyle="--", linewidth=1)
ax.axvline(lo, color=COLORS["example"], linestyle="--", linewidth=1)
ax.set_xticks([lo, 100, hi, 101, 102], ["99.02", "100", "100.98", "\n101", "102"])
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.set_ylim(0, 1.45)  # 上に凡例の場所をあける
ax.set_xlabel("標本平均 $\\bar{X}$（g）")
ax.legend(frameon=False, loc="upper left", fontsize=7, ncol=2)
save(fig, "prep_power")

# ---------------------------------------------------------------- 両側と片側
setup()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(FULL_WIDTH, FULL_WIDTH * 0.3))
for ax, regions, ticks, title in [
    (ax1, [z >= 1.96, z <= -1.96], [-1.96, 0, 1.96], "両側検定（$H_1: \\mu \\neq \\mu_0$）"),
    (ax2, [z >= 1.645], [0, 1.645], "片側検定（$H_1: \\mu > \\mu_0$）"),
]:
    ax.plot(z, phi, color=COLORS["main"])
    for r in regions:
        ax.fill_between(z[r], phi[r], color=COLORS["theorem"], alpha=0.4, linewidth=0)
    ax.set_xticks(ticks, [f"{t:g}".replace("-", "−") for t in ticks])
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_title(title)
ax1.text(2.6, 0.07, "0.025", fontsize=8, ha="center", color=COLORS["theorem"])
ax1.text(-2.6, 0.07, "0.025", fontsize=8, ha="center", color=COLORS["theorem"])
ax2.text(2.4, 0.09, "0.05", fontsize=8, ha="center", color=COLORS["theorem"])
fig.tight_layout()
save(fig, "prep_one_two_sided")
