#!/usr/bin/python
from Bio import SeqIO
def rename_seqs(fasta_path, seq_name):
    out_csv_path = fasta_path[:-6] + ".csv"
    out_fasta = fasta_path[:-6] + "_renamed.fasta"
    results = []
    i = 0
    with open(out_csv_path, "w") as out_csv:
        for record in SeqIO.parse(fasta_path, "fasta"):
            i+=1
            old_id = record.id
            new_id = seq_name + str(i)
            record.id = new_id
            results.append(record)
            out_csv.write('{},{}\n'.format(old_id,new_id))
    SeqIO.write(results, out_fasta, "fasta")
    return 0

fasta = "/media/anna/data/anna_drive/projects/diplonemids/diplonema/Proteins_and_Transcripts_201604/proteins_SL.faa"
seq_name = "dpapi_"
rename_seqs(fasta, seq_name)
