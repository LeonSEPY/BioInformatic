from Bio import SeqIO

def count_nucleotides(fasta_path):
    record = SeqIO.read(fasta_path, "fasta")
    sequence = record.seq.upper()
    counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "C": sequence.count("C"),
        "G": sequence.count("G")
    }
    return counts

if __name__ == "__main__":
    fasta_file = "sequence.fasta"
    frequencies = count_nucleotides(fasta_file)
    print("Nucleotide frequencies:")
    for nucleotide, count in frequencies.items():
        print(f"{nucleotide}: {count}")
