class GenomicRegion:
    def __init__(self, name, start, end, strand="+"):
        self.name = name
        self.start = start
        self.end = end
        self.strand = strand

    def length(self):
        return self.end - self.start + 1

    def __str__(self):
        return f"{self.name}: {self.start}-{self.end} ({self.strand})"

if __name__ == "__main__":
    region = GenomicRegion("GeneX", 100, 500)
    print(region)
    print("Length:", region.length())
