import HTSeq

def count_reads(gtf_file, bam_file):
    """
    Counts reads mapped to genes using HTSeq.
    """
    gtf = HTSeq.GFF_Reader(gtf_file)
    features = HTSeq.GenomicArrayOfSets("auto", stranded=False)

    for feature in gtf:
        if feature.type == "exon":
            features[feature.iv] += feature.attr["gene_id"]

    counts = {}
    aln_file = HTSeq.BAM_Reader(bam_file)
    for aln in aln_file:
        if not aln.aligned:
            continue
        gene_ids = set()
        for iv, val in features[aln.iv].steps():
            gene_ids |= val
        if len(gene_ids) == 1:
            gene_id = list(gene_ids)[0]
            counts[gene_id] = counts.get(gene_id, 0) + 1

    return counts

if __name__ == "__main__":
    gtf_path = "example.gtf"
    bam_path = "example.bam"
    print("Counting reads mapped to genes...")
    counts = count_reads(gtf_path, bam_path)
    for gene, count in counts.items():
        print(f"{gene}: {count}")
