# DNA Toolset/Code testing file

from DNAToolkit import *
from utilities import colored
import random

#Creating a random DNA sequence for testing:
rnd_dna_str = ''.join([random.choice(Nucleotides)
                    for nuc in range(50)])

                        



#rnd_dna_str = "ATCCTGATT"

#print(validateSeq(rnd_dna_str))
#print(countNucFrequency(rnd_dna_str))


print(f'\nSequence: {rnd_dna_str}\n')
print(f'[1] + Sequence Length: {len(rnd_dna_str)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(rnd_dna_str)}\n')

print(f'[3] + DNA/RNA Transcription: {transcription(rnd_dna_str)}\n')

print(f"[4] + DNA String + Complement + Reverse Complement:\n5' {rnd_dna_str} 3'")
print(f"   {''.join(['|' for c in range(len(rnd_dna_str))])}")
print(f"3' {reverse_complement(rnd_dna_str)[::-1]} 5' [Complement]")
print(f"5' {reverse_complement(rnd_dna_str)} 3' [Rev. Complement]\n")
 
print(f'[5] + GC Content: {gc_content(rnd_dna_str)}%\n')


