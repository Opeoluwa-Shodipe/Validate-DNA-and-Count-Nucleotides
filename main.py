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


print(f'\nSequence: {colored(rnd_dna_str)}\n')
print(f'[1] + Sequence Length: {len(rnd_dna_str)}\n')
print(colored(f'[2] + Nucleotide Frequency: {countNucFrequency(rnd_dna_str)}\n'))
print(f'[3] + DNA -> RNA {transcription(rnd_dna_str)}\n')

print(f"[4] + DNA String + Reverse Complement:\n5' {rnd_dna_str} 3'")
print(f"   {''.join(['|' for c in range(len(rnd_dna_str))])}")
print(f"3' {colored(reverse_complement(rnd_dna_str))} 5'\n")


