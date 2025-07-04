from graphviz import Digraph
import os

def draw_causal_dag():
    dot = Digraph(comment='Causal DAG: NO2 → RH')

    # Nodes
    dot.node('T', 'Temperature')
    dot.node('C', 'CO (Carbon Monoxide)')
    dot.node('X', 'NO2 (Treatment)')
    dot.node('Y', 'RH (Relative Humidity)')
    dot.node('S', 'Time/Season')

    # Edges
    dot.edge('S', 'T')
    dot.edge('S', 'C')
    dot.edge('S', 'X')
    dot.edge('S', 'Y')
    dot.edge('C', 'X')
    dot.edge('T', 'Y')
    dot.edge('C', 'Y')
    dot.edge('X', 'Y')  # Main causal effect

    base_dir = os.path.dirname(os.path.dirname(__file__))
    output_dir = os.path.join(base_dir, 'outputs', 'figures')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'causal_dag')

    dot.render(output_path, format='png', cleanup=True)
    print(f"DAG saved to {output_path}.png")

if __name__ == "__main__":
    draw_causal_dag()
