# DNA Toolset/Code testing file

from DNAToolkit import *
import random

#Creating a random DNA sequence for testing:
rnd_dna_str = ''.join([random.choice(Nucleotides)
                    for nuc in range(50)])

                        



#rnd_dna_str = "ATCCTGATT"

print(validateSeq(rnd_dna_str))
print(countNucFrequency(rnd_dna_str))

