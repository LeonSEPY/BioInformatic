import matplotlib.pyplot as plt

def plot_nucleotide_distribution(sequence):
    sequence = sequence.upper()
    counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "C": sequence.count("C"),
        "G": sequence.count("G")
    }
    plt.bar(counts.keys(), counts.values())
    plt.title("Nucleotide Frequency")
    plt.xlabel("Nucleotide")
    plt.ylabel("Count")
    plt.show()

if __name__ == "__main__":
    with open("sequence.fasta", "r") as f:
        lines = f.readlines()
        sequence = "".join([line.strip() for line in lines if not line.startswith(">")])
    plot_nucleotide_distribution(sequence)
