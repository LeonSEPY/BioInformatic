from Bio import SeqIO

def read_fasta(fasta_path):
    record = SeqIO.read(fasta_path, "fasta")
    print(f"ID: {record.id}")
    print(f"Description: {record.description}")
    print(f"Sequence: {record.seq}")

if __name__ == "__main__":
    read_fasta("sequence.fasta")
