CODON_DICT = {
    'Methionine': ['AUG'],
'Phenylalanine' : ['UUU', 'UUC'],
'Leucine' : ['UUA', 'UUG'],
'Serine' : ['UCU', 'UCC', 'UCA', 'UCG'],
'Tyrosine' : ['UAU', 'UAC'],
'Cysteine' : ['UGU', 'UGC'],	
'Tryptophan' : ['UGG'],
'STOP' : ['UAA', 'UAG', 'UGA']
}
def proteins(strand):
    result = []
    for i in range(0, len(strand), 3):
        substring = strand[i:i+3]
        for key, value in CODON_DICT.items():
            if substring in value:
                result.append(key)
    for i, j in enumerate(result):
        if j == 'STOP':
            result = result[:i]
    return result