import matplotlib.pyplot as plt

def dot_plot(seq1, seq2):
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                plt.plot(j, i, 'ko')
    plt.xlabel("Sequence 2")
    plt.ylabel("Sequence 1")
    plt.title("Dot Plot")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    seq1 = input("Enter first sequence: ").upper()
    seq2 = input("Enter second sequence: ").upper()
    dot_plot(seq1, seq2)
