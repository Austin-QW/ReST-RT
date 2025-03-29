import matplotlib.pyplot as plt
import numpy as np

# Data from your table
models = ['Llama-3.2-3B-Instruct', 'Qwen2.5-3B-Instruct']
steps = [1000, 2000, 3000, 4000, 5000, 6000, 6750]

# Metrics data: [d2p, p2d, p2d_reverse, d2p_reverse]
llama_data = np.array([
    [74, 33, 15.33, 3.33],
    [82, 43.33, 16.33, 8.33],
    [76.33, 50, 10.67, 11.67],
    [83, 50.67, 14, 11.33],
    [78.67, 50.33, 15.33, 13],
    [79.67, 50, 12.33, 14],
    [78.67, 49.67, 14.67, 14]
])

qwen_data = np.array([
    [68.67, 29.33, 3, 2],
    [77.67, 39.67, 8.3, 5.3],
    [80.67, 39.33, 8.67, 7],
    [77.67, 41.33, 7.67, 6.67],
    [71, 41, 7.33, 8],
    [71.33, 42.33, 6.67, 8.33],
    [70.67, 41.67, 6.33, 10]  
])

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
        ax.set_ylim(0, 17)  # Focus on the relevant range
    
    ax.legend()

plt.tight_layout()
plt.savefig('combined.png', dpi=300, bbox_inches='tight')
plt.show()
