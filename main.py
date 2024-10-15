def to_rna(dna_strand):
    rna_complement = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    return ''.join(rna_complement[letter] for letter in dna_strand)