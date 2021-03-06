# This files contains a few functions for basic manipulation of deoxyribonucleic acid (DNA) sequence

def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for char in dna:
        if char == nucleotide:
            count = count + 1
    return count


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return ( dna2 in dna1)

def is_valid_sequence (dna):
    '''(str) -> bool

    Return True if the dna sequence only contains A, T, C or G
    
    >>> is_valid_sequence ('ATCGT')
    True
    >>> is_valid_sequence ('abcd')
    False
    '''
    for char in dna:
        if not (char in 'ATCG'):
           return False
    return True

def insert_sequence (dna1, dna2, num):
    '''(str, str, int) -> str

    Return True if the dna sequence only contains A, T, C or G
    
    >>> insert_sequence ('abcdef', 'A', 3)
    abcAdef
    
    '''
    
    return dna1[:num]+dna2+dna1[num:]

def get_complement (nucleotide):
    '''(str) -> str

    return a string that is complement to nudleotide
    '''
    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'G':
        return 'C'

def get_complement_sequence (dna):
    '''(str) -> str

    return a string that is complement to dna
    '''
    if is_valid_sequence (dna):
        comp = ''
        for char in dna:
            comp = comp + get_complement (char)
        return comp