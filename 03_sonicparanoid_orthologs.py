import pandas as pd

def infer_orthologs(blast_output_files):
    """
    Simulates ortholog inference by finding reciprocal best hits from multiple BLAST result files.
    Each BLAST output must be in tabular format: query, subject, identity, etc.
    """
    best_hits = {}

    for file in blast_output_files:
        df = pd.read_csv(file, sep="\t", header=None)
        df.columns = ["query", "subject", "identity", "alignment_length", "mismatches", "gap_opens",
                      "q_start", "q_end", "s_start", "s_end", "evalue", "bit_score"]
        species = file.split(".")[0]
        best_hits[species] = df.groupby("query").first().reset_index()

    # Simulate RBH (reciprocal best hits) check between species A and B
    species_list = list(best_hits.keys())
    if len(species_list) < 2:
        print("At least two species needed for RBH.")
        return []

    A, B = species_list[0], species_list[1]
    df_A = best_hits[A]
    df_B = best_hits[B]

    ortholog_pairs = []
    for _, row in df_A.iterrows():
        query = row["query"]
        subject = row["subject"]
        reciprocal = df_B[df_B["query"] == subject]
        if not reciprocal.empty and reciprocal.iloc[0]["subject"] == query:
            ortholog_pairs.append((query, subject))

    return ortholog_pairs

if __name__ == "__main__":
    blast_files = ["speciesA_vs_speciesB.tsv", "speciesB_vs_speciesA.tsv"]
    orthologs = infer_orthologs(blast_files)
    print("Reciprocal Best Hits (Putative Orthologs):")
    for pair in orthologs:
        print(f"{pair[0]} <--> {pair[1]}")
