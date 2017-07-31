from Bio import SeqIO
from Bio.Seq import Seq
for seq_record in SeqIO.parse("PSORS1.fasta", "fasta"):
	print("A:",seq_record.seq.count("A"))
	print("T",seq_record.seq.count("T"))
	print("C",seq_record.seq.count("C"))
	print("G",seq_record.seq.count("G"))
	print("\n")
for seq_record1 in SeqIO.parse("PSORS2.fasta", "fasta"):
	print("A:",seq_record1.seq.count("A"))
	print("T",seq_record1.seq.count("T"))
	print("C",seq_record1.seq.count("C"))
	print("G",seq_record1.seq.count("G"))
	print("\n")
for seq_record2 in SeqIO.parse("PSORS4.fasta", "fasta"):
	print("A:",seq_record2.seq.count("A"))
	print("T",seq_record2.seq.count("T"))
	print("C",seq_record2.seq.count("C"))
	print("G",seq_record2.seq.count("G"))
	print("\n")
for seq_record3 in SeqIO.parse("PSORS5.fasta", "fasta"):
	print("A:",seq_record3.seq.count("A"))
	print("T",seq_record3.seq.count("T"))
	print("C",seq_record3.seq.count("C"))
	print("G",seq_record3.seq.count("G"))