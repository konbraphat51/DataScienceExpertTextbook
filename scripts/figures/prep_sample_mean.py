"""第1章：サイコロの目の標本平均の分布。n を大きくすると、平均 3.5 のまわりに集まる。"""

import matplotlib.pyplot as plt
import numpy as np

from figstyle import COLORS, FULL_WIDTH, save, setup

# n 個の目の和の分布を、1 個の分布のたたみこみで正確に求める
die = np.full(6, 1 / 6)  # 目 1〜6 の確率

setup()
fig, axes = plt.subplots(1, 3, figsize=(FULL_WIDTH, FULL_WIDTH * 0.3), sharey=False)
for ax, n in zip(axes, (1, 4, 16)):
    pmf = die.copy()
    for _ in range(n - 1):
        pmf = np.convolve(pmf, die)
    sums = np.arange(n, 6 * n + 1)
    means = sums / n
    # 棒の面積が確率になるように、高さを「確率 ÷ 刻み幅 (1/n)」にする
    ax.bar(means, pmf * n, width=0.8 / n, color=COLORS["main"])
    sd = np.sqrt(35 / 12 / n)
    ax.set_title(f"$n = {n}$（標準偏差 {sd:.2f}）")
    ax.set_xlim(0.5, 6.5)
    ax.set_xticks(range(1, 7))
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.axvline(3.5, color=COLORS["theorem"], linestyle="--", linewidth=1)
    ax.set_xlabel("標本平均 $\\bar{X}$")

fig.tight_layout()
save(fig, "prep_sample_mean")
