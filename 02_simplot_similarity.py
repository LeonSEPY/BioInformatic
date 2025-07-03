import matplotlib.pyplot as plt
from Bio import SeqIO

def sliding_window_similarity(query_seq, ref_seq, window_size=50, step_size=10):
    """
    Computes percent identity in a sliding window between two sequences.
    """
    similarities = []
    positions = []
    for i in range(0, len(query_seq) - window_size + 1, step_size):
        window_query = query_seq[i:i+window_size]
        window_ref = ref_seq[i:i+window_size]
        matches = sum(1 for a, b in zip(window_query, window_ref) if a == b)
        identity = matches / window_size * 100
        similarities.append(identity)
        positions.append(i + window_size // 2)
    return positions, similarities

def plot_similarity_curve(positions, similarities, title="Similarity Plot"):
    plt.plot(positions, similarities, label="Percent Identity")
    plt.title(title)
    plt.xlabel("Position")
    plt.ylabel("Identity (%)")
    plt.ylim(0, 100)
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    query_record = SeqIO.read("query.fasta", "fasta")
    ref_record = SeqIO.read("reference.fasta", "fasta")
    positions, similarity = sliding_window_similarity(str(query_record.seq), str(ref_record.seq))
    plot_similarity_curve(positions, similarity, title="SimPlot++ Style Similarity")
