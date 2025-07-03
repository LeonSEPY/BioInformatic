def count_pattern(sequence, pattern):
    count = 0
    for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i:i+len(pattern)] == pattern:
            count += 1
    return count

if __name__ == "__main__":
    with open("sequence.fasta", "r") as f:
        lines = f.readlines()
        sequence = "".join([line.strip() for line in lines if not line.startswith(">")])
    pattern = input("Enter the pattern to search for: ").upper()
    result = count_pattern(sequence.upper(), pattern)
    print(f"The pattern '{pattern}' appears {result} times.")
