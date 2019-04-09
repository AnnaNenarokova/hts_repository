#!python3
import csv
from os import listdir
from Bio import SeqIO
def parse_metadata(metadata_path):
    parsed_data = {}
    with open (metadata_path) as metadata_f:
        metadata = csv.DictReader(metadata_f)
        for row in metadata:
            file_name = row["file_name"]
            species_name = row["species_name"]
            species_code = row["species_code"]
            taxid = row["taxid"]
            parsed_data[file_name] = {
            "species_code": species_code,
            "species_name": species_name,
            "taxid": taxid
            }
    return parsed_data

seqdir_path = "/home/shared/BANK/diplonema_dataset/all_refs/"
metadata_path = "/home/shared/BANK/diplonema_dataset/all_refdataset.csv"
seqdata_path = "/projects/Diplonema_genome_evolution/refdataset_diplonema/dpapi_refdataset_info.csv"
fasta_outpath = "/projects/Diplonema_genome_evolution/refdataset_diplonema/dpapi_refdataset.faa"

metadata = parse_metadata(metadata_path)

result_records = []
result_data = [["new_id", "old_id", "taxid", "species_code", "species_name"]]

for seqfile in listdir(seqdir_path):
    if seqfile in metadata.keys():
        print (seqfile)
        seqfile_path = seqdir_path + seqfile
        i = 0
        for record in SeqIO.parse(seqfile_path, "fasta"):
            i += 1
            old_id = record.id
            old_description = record.description
            taxid = metadata[seqfile]["taxid"]
            species_code = metadata[seqfile]["species_code"]
            species_name = metadata[seqfile]["species_name"]
            new_id = species_code + "_" + species_name + "_{:05d}".format(i)
            new_description = 'old_id:{}\ttaxid:{}\tdescription:{}'.format(old_id, taxid,old_description)
            new_record = record
            new_record.id = new_id
            new_record.description = new_description
            result_records.append(new_record)
            result_data.append([new_id, old_id, taxid, species_code, species_name])
    else:
        print(seqfile + " is not in the metadata!\n")

print ("writing seqs")
SeqIO.write(result_records, fasta_outpath, "fasta")

print ("writing info")
with open(seqdata_path, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(result_data)
