import json
import webbrowser
import colorcet as cc
import platform
import os

# from IPython.core.display import display, HTML

def visualize_graph(data, html_file="graph.html"):
    """
    Visualizes a graph in 3D using 3d-force-graph.

    Parameters:
    - data: A data object containing node labels and edge indices.
    - html_file: The name of the HTML file to be generated and opened in a web browser.
    """
    # Generate color map based on labels
    max_label = data.y.max().item()
    color_map = cc.glasbey_light[:max_label + 1]

    # Prepare nodes and links for visualization
    nodes = [{"id": str(i), "color": color_map[label.item()]} for i, label in enumerate(data.y)]
    links = [{"source": str(u), "target": str(v)} for u, v in zip(*data.edge_index.tolist())]
    graph_data = {"nodes": nodes, "links": links}

    # Create HTML content
    html_str = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>3D Force Graph</title>
    </head>
    <body>
    <script src="https://unpkg.com/3d-force-graph"></script>
    <div id="3d-graph"></div>
    <script>
      var graphData = {json.dumps(graph_data)};
      var graph = ForceGraph3D()(document.getElementById('3d-graph'))
        .graphData(graphData)
        .nodeColor('color');
    </script>
    </body>
    </html>
    """

    # Write HTML to file and open it
    with open(html_file, "w") as file:
        file.write(html_str)
    

    # Open the HTML file in the default web browser
    if platform.system() == 'Darwin':  # macOS
        os.system(f'open {html_file}')
    else:  # Linux and Windows
        webbrowser.open(f'file://{os.path.realpath(html_file)}')

