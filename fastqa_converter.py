'''
This program help to convert DNA sequences obtained from next generation sequencing.
After conversion, the raw data are ready for analysis by tools provided on NCBI Genome Workbench.
'''
from Bio import SeqIO

SeqIO.convert('input.fastq','fastq','output.fasta','fasta')