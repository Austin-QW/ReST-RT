import matplotlib.pyplot as plt
import numpy as np

# Data from your table
models = ['Llama-3.2-3B-Instruct', 'Qwen2.5-3B-Instruct']
steps = [1000, 2000, 3000, 4000, 4500]

# Metrics data: [d2p, p2d, p2d_reverse, d2p_reverse]
llama_data = [
    [87.67, 45.67, 0, 5],
    [80.67, 47, 0, 10],
    [81, 48.67, 0, 10],
    [82.67, 48.67, 0, 12.33],
    [82, 47.67, 0, 11.67]
]

qwen_data = [
    [70.33, 30, 0, 3],
    [70.67, 30.33, 0, 4],
    [77.67, 34.67, 0, 4.33],
    [80, 36.33, 0, 4.33],
    [79, 35.66, 0, 5]
]

# Create figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
# fig.suptitle('Exact Match Scores Across Training Steps', fontsize=16)

metrics = ['D2P', 'P2D', 'P2D Reverse', 'D2P Reverse']
colors = ['#1f77b4', '#ff7f0e']  # Colorblind-friendly palette

# Plot each metric
for i, ax in enumerate(axes.flat):
    metric = metrics[i]
    ax.set_title(metric, fontweight='bold')
    ax.set_xlabel('Training Steps')
    ax.set_ylabel('Score (%)')
    ax.grid(True, linestyle='--', alpha=0.6)
    
    # Plot data
    ax.plot(steps, [x[i] for x in llama_data], 
            marker='o', color=colors[0], linewidth=2, 
            label='Llama-3.2-3B-Instruct')
    ax.plot(steps, [x[i] for x in qwen_data], 
            marker='s', color=colors[1], linewidth=2,
            label='Qwen2.5-3B-Instruct')
    
    # Special handling for reverse metrics (0 values)
    if 'Reverse' in metric:
        ax.set_ylim(0, 15)  # Focus on the relevant range
    
    ax.legend()

plt.tight_layout()
plt.savefig('p2d.png', dpi=300, bbox_inches='tight')
plt.show()