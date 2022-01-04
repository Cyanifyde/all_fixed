"""
3-letter sequences encode amino acids in DNA. For example, TTT is phenylalanine and TTA is leucine. Write a program that reads a DNA sequence stored in a file and outputs the number of a particular amino acid in the sequence requested by the user. E.g. in the sequence: ACGTTTGTATTT the sequence TTT appears twice.
Data you can use:
ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCC
CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCGGA
CTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG
"""
from _runhelp import ff
v=ff("amino.txt")[0]
g=open(v,"r").read()
count_ttt=g.count("TTT")
count_tta=g.count("TTA")
print("there is {} TTT's\nand there are {} TTA's".format(count_ttt,count_tta))