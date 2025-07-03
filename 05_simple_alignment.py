def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
    n = len(seq1)
    m = len(seq2)
    score = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        score[i][0] = i * gap
    for j in range(m+1):
        score[0][j] = j * gap
    for i in range(1, n+1):
        for j in range(1, m+1):
            match_score = score[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            delete = score[i-1][j] + gap
            insert = score[i][j-1] + gap
            score[i][j] = max(match_score, delete, insert)
    return score[n][m]

if __name__ == "__main__":
    seq1 = input("Enter first sequence: ").upper()
    seq2 = input("Enter second sequence: ").upper()
    print(f"Alignment score: {needleman_wunsch(seq1, seq2)}")
