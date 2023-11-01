#!python3
from ete3 import Tree

# Function to format a tree node
def format_tree(node, indent=0):
    formatted_tree = ""
    if not node.is_leaf():
        formatted_tree += "(\n"
        for child in node.children:
            formatted_tree += " " * (indent + 2) + format_tree(child, indent + 2)
            if child != node.children[-1]:
                formatted_tree += ",\n"
        formatted_tree += "\n" + " " * indent + ")"
    formatted_tree += node.name
    return formatted_tree

# Function to read a tree from an input file, format it, and write it to an output file
def format_tree_file(input_file_path, output_file_path):
    try:
        # Read the Newick tree from the input file
        with open(input_file_path, "r") as input_file:
            newick_str = input_file.read().strip()

        # Create a Tree object from the Newick string
        tree = Tree(newick_str)

        # Format the tree
        formatted_tree = format_tree(tree)

        # Write the formatted tree to the output file
        with open(output_file_path, "w") as output_file:
            output_file.write(formatted_tree)

        print(f"Formatted tree has been written to '{output_file_path}'")

    except FileNotFoundError:
        print(f"Error: The input file '{input_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Input and output file paths
input_file_path = "/Users/vl18625/work/euk/trees/test/aebe_manual_sorted.tree"
output_file_path = "/Users/vl18625/work/euk/trees/test/aebe_manual_sorted_tab_formatted.tree"

# Call the function to format the tree and write it to the output file
format_tree_file(input_file_path, output_file_path)
