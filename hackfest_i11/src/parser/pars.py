import ast

def print_tree(node, level=0):
    print(' ' * level + str(node.__class__.__name__))
    for child in ast.iter_child_nodes(node):
        print_tree(child, level + 1)

with open("parsing.py", "r") as file:
    source = file.read()

tree = ast.parse(source)
print_tree(tree)
