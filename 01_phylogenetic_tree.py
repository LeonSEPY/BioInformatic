from Bio import Phylo
from io import StringIO

def create_phylogenetic_tree():
    """
    Creates and displays a simple phylogenetic tree from a Newick string.
    """
    newick = "((Human,Chimpanzee),Gorilla);"
    tree = Phylo.read(StringIO(newick), "newick")

    print("Phylogenetic Tree:")
    Phylo.draw_ascii(tree)

if __name__ == "__main__":
    create_phylogenetic_tree()
