"""第1章：30 人のテストの点数のヒストグラムと箱ひげ図（同じ横軸で上下に並べる）。"""

import matplotlib.pyplot as plt
import numpy as np

from figstyle import COLORS, WIDTH, save, setup

scores = np.array([62, 75, 48, 81, 69, 55, 90, 73, 66, 58, 77, 84, 71, 39, 64,
                   68, 79, 52, 87, 70, 61, 74, 95, 57, 67, 72, 83, 46, 65, 76])

setup()
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(WIDTH, WIDTH * 0.7), sharex=True,
    gridspec_kw={"height_ratios": [3, 1], "hspace": 0.08},
)

ax1.hist(scores, bins=range(30, 101, 10), color=COLORS["main"], alpha=0.35,
         edgecolor=COLORS["main"])
ax1.set_ylabel("度数（人）")
ax1.set_yticks(range(0, 11, 2))

# 箱ひげ図（四分位数は「下半分・上半分の中央値」で計算した値を使う）
q1, med, q3 = 61, 69.5, 77
stats = [{"whislo": scores.min(), "q1": q1, "med": med, "q3": q3,
          "whishi": scores.max(), "fliers": []}]
ax2.bxp(stats, orientation="horizontal", widths=0.6, patch_artist=True,
        boxprops={"facecolor": COLORS["main"] + "33", "edgecolor": COLORS["main"]},
        medianprops={"color": COLORS["theorem"], "linewidth": 2},
        whiskerprops={"color": COLORS["main"]}, capprops={"color": COLORS["main"]})
ax2.set_yticks([])
ax2.spines["left"].set_visible(False)
for v, name in [(scores.min(), "最小値"), (q1, "$Q_1$"), (med, "中央値"),
                (q3, "$Q_3$"), (scores.max(), "最大値")]:
    ax2.annotate(name, (v, 1.35), ha="center", fontsize=7, color=COLORS["example"])
ax2.set_ylim(0.5, 1.6)
ax2.set_xlabel("点数")
ax2.set_xticks(range(30, 101, 10))

save(fig, "prep_hist_box")
