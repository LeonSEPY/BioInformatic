def calculate_gc_content(sequence):
    g = sequence.count("G")
    c = sequence.count("C")
    gc_content = (g + c) / len(sequence) * 100
    return gc_content

if __name__ == "__main__":
    with open("sequence.fasta", "r") as f:
        lines = f.readlines()
        sequence = "".join([line.strip() for line in lines if not line.startswith(">")])
    gc = calculate_gc_content(sequence.upper())
    print(f"GC Content: {gc:.2f}%")
