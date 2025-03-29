import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 原始数据整理
data = {
    "Llama-3.2-3B-Instruct": {
        "Original Dataset":          [99.67, 53.33, 0.00, 0.00],
        "D2P Augmented Dataset":     [96.67, 49.67, 16.00, 0.00],
        "P2D Augmented Dataset":     [82.00, 47.67, 0.00, 11.67],
        "Bidirectional Integrated":  [78.67, 49.67, 14.67, 14.00]
    },
    "Qwen2.5-3B-Instruct": {
        "Original Dataset":          [22.00, 22.00, 0.00, 0.00],
        "D2P Augmented Dataset":     [60.67, 22.00, 0.30, 0.00],
        "P2D Augmented Dataset":     [79.00, 35.66, 0.00, 5.00],
        "Bidirectional Integrated":  [70.67, 41.67, 6.33, 10.00]
    }
}

tasks = ['d2p', 'p2d', 'p2d_reverse', 'd2p_reverse']
datasets = list(data["Llama-3.2-3B-Instruct"].keys())
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
markers = ['o', 's', '^', 'D']

def plot_model_performance(model_name):
    plt.figure(figsize=(10, 6))
    
    for dataset_idx, (dataset, scores) in enumerate(data[model_name].items()):
        x = np.arange(len(tasks)) 
        plt.scatter(x, scores, 
                   s=100,
                   color=colors[dataset_idx],
                   marker=markers[dataset_idx],
                   label=dataset,
                   edgecolors='black')
    
    plt.title(f'{model_name} Performance Comparison', fontsize=14)
    plt.xticks(np.arange(len(tasks)), tasks, rotation=45, ha='right')
    plt.ylabel('Score (%)', fontsize=12)
    plt.ylim(-5, 105)
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.show()

# 生成两个模型的图表
plot_model_performance("Llama-3.2-3B-Instruct")
plt.savefig('p2d.png', dpi=300, bbox_inches='tight')
plot_model_performance("Qwen2.5-3B-Instruct")