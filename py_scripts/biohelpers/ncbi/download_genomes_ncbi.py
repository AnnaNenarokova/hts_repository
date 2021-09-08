#!python3
import sys
from encoder import XML2Dict
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"

def get_assemblies_dict(genome_id_list):
    elink_records = Entrez.read(Entrez.elink(dbfrom="genome", db="assembly", id=genome_id_list))
    assemblies_dict = {}
    for record in elink_records:
        id_list = record['IdList']
        if len (id_list) == 0:
            print ("id_list is empty!")
            sys.exit(1)
        elif len(id_list) > 1:
            print ("id_list contains several elements:", id_list)
        genome_id = record['IdList'][0]

        link_list = record['LinkSetDb']
        if len (link_list) == 0:
            print ("link_list is empty!")
            sys.exit(1)
        elif len(id_list) > 1:
            print ("link_list contains several elements:", id_list)
        link = link_list[0]

        id_dict_list = link["Link"]
        if len (id_dict_list) == 0:
            print ("id_dict is empty!")
            sys.exit(1)
        else:
            id_list = []
            for id_dict in id_dict_list:
                id_list.append(id_dict['Id'])
            assemblies_dict[genome_id] = id_list
    return assemblies_dict

def choose_best_assembly(ncbi_assembly_records):
    best_assembly = ncbi_assembly_records[0]
    for assembly in ncbi_assembly_records:
        if assembly["RefSeq_category"] in [b"reference genome", b"representative genome"]:
            best_assembly = assembly
            break
        elif (assembly["PartialGenomeRepresentation"] == b'false' and not bool(assembly["AnomalousList"])):
            best_rank = int(best_assembly["AssemblyStatusSort"])
            current_rank = int(assembly["AssemblyStatusSort"])
            if current_rank < best_rank:
                best_assembly = assembly
            elif current_rank == best_rank:
                best_N50 = int(best_assembly["ContigN50"])
                current_N50 = int(assembly["ContigN50"])
                if current_N50 > best_N50:
                    best_assembly = assembly
    return best_assembly

def get_best_assembly(assemblies_list):
    best_assembly_id = 0
    if len(assemblies_list) == 1:
        best_assembly_id = assemblies_list[0]
    else:
        assembly_ids = ",".join(assemblies_list)
        ncbi_xml = Entrez.esummary(db="assembly", id=assembly_ids, retmode="xml").read()
        ncbi_dict = XML2Dict().parse(ncbi_xml)
        ncbi_assembly_records = ncbi_dict['eSummaryResult']['DocumentSummarySet']['DocumentSummary']
        best_assembly = choose_best_assembly(ncbi_assembly_records)
        best_assembly_id = best_assembly['#DocumentSummary']['uid']
    return best_assembly_id

genome_id_list = [11136, 3258, 2529, 1115, 167]

assemblies_dict = get_assemblies_dict(genome_id_list)
best_assembly_ids = []

for genome in assemblies_dict:
    best_assembly_id = get_best_assembly(assemblies_dict[genome])
    best_assembly_ids.append(best_assembly_id)
