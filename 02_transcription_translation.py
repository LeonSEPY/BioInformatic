from Bio.Seq import Seq
from Bio import SeqIO

def transcribe_and_translate(fasta_path):
    record = SeqIO.read(fasta_path, "fasta")
    dna_seq = record.seq
    rna_seq = dna_seq.transcribe()
    protein_seq = rna_seq.translate(to_stop=True)
    return rna_seq, protein_seq

if __name__ == "__main__":
    fasta_file = "sequence.fasta"
    rna, protein = transcribe_and_translate(fasta_file)
    print("RNA Sequence:")
    print(rna)
    print("\nProtein Sequence:")
    print(protein)
