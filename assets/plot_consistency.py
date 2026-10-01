"""Redraw the camera-ready reward-consistency tables; no new measurements."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12, 'axes.spines.top': False, 'axes.spines.right': False})
methods = ['Direct PRM', 'RaR', 'SCRIBE']
values = [[71.8, 82.4, 93.7], [58.6, 69.4, 86.8]]
titles = ['Same input, repeated evaluation', 'Similar subgoals, different problems']
fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), sharey=True)
for ax, vals, title in zip(axes, values, titles):
    bars=ax.bar(methods, vals, color=['#CBD5E1', '#A5B4FC', '#4F46E5'], width=.58)
    ax.set_ylim(0, 105)
    ax.set_yticks(np.arange(0, 101, 20))
    ax.set_title(title, fontsize=13, pad=17, fontweight='bold')
    ax.grid(axis='y', alpha=.18)
    ax.set_axisbelow(True)
    for bar, v in zip(bars, vals):
        ax.text(bar.get_x()+bar.get_width()/2, v+2, f'{v:.1f}%', ha='center', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Exact reward agreement (%) ↑')
fig.tight_layout(pad=2)
fig.savefig(Path(__file__).with_name('reward-consistency.png'), dpi=200, facecolor='white')
fig.savefig(Path(__file__).with_name('reward-consistency.pdf'), facecolor='white')
