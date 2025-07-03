import random

def mutate_sequence(sequence, num_mutations=3):
    sequence = list(sequence.upper())
    bases = ["A", "T", "C", "G"]
    for _ in range(num_mutations):
        pos = random.randint(0, len(sequence)-1)
        new_base = random.choice([b for b in bases if b != sequence[pos]])
        sequence[pos] = new_base
    return "".join(sequence)

if __name__ == "__main__":
    with open("sequence.fasta", "r") as f:
        lines = f.readlines()
        sequence = "".join([line.strip() for line in lines if not line.startswith(">")])
    print("Mutated Sequence:", mutate_sequence(sequence))
