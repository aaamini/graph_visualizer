# graph_visualizer

A package for visualizing graphs from `torch_geometric` datasets using 3d-force-graph.

## Installation

You can install the package directly from the GitHub repository:

```bash
pip install git+https://github.com/aaamini/graph_visualizer.git
```

## Example usage

```python
from graph_visualizer import visualize_graph
import torch_geometric.datasets as datasets

# Example data
dataset = datasets.KarateClub()  # Or any other dataset you have
data = dataset[0]

# Visualize the graph
visualize_graph(data)
```

